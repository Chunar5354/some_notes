## JDBC

### 通过驱动包的方式使用依赖

#### 下载驱动

在Java中访问mysql需要借助`JDBC`实现，并且需要首先安装驱动包

安装包可以在[这里](https://dev.mysql.com/downloads/connector/j/)下载，注意要在下拉菜单中选择`Platform Independent`

下载后解压文件得到`.jar`文件

#### 加载驱动

- 在vscode中的加载方式

首先需要安装一个Java的插件集合`Project Manager for Java`

安装之后点击左下角`JAVA PROJECT`中的`Referenced Libraries`右侧的加号，将上面的jar文件加载进来

[![Ob9huD.png](https://s1.ax1x.com/2022/05/19/Ob9huD.png)](https://imgtu.com/i/Ob9huD)

- 在IDEA中的加载方式

`File` -> `Project Structure` -> `Modules` -> `点击加号` -> `JARs or Directories` -> 选择路径导入本地jar包

[![XukQKO.png](https://s1.ax1x.com/2022/05/28/XukQKO.png)](https://imgtu.com/i/XukQKO)

### 通过maven管理依赖

再IDEA中，编写pom.xml：

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

### 编写代码

JDBC使用的基本流程：

- 1.实例化驱动

```java
Class.forName("com.mysql.cj.jdbc.Driver");
```

- 2.创建连接

```java
// 需要数据库服务端的信息
// url解释为："jdbc:数据库类型:IP:端口/数据库?是否使用SSL & 是否允许客户端从服务器获取公钥 & 时区 & 编码方式（中文不乱码）"
static final String DB_URL = "jdbc:mysql://hostname:3306/lottery?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC&characterEncoding=UTF-8";
static final String USER = "user";
static final String PASS = "password";

conn = DriverManager.getConnection(DB_URL, USER, PASS);
stmt = conn.createStatement();  // 连接实例化
```

- 3.执行sql语句

```java
sql = "SELECT * FROM table.";
ResultSet rs = stmt.executeQuery(sql);
while (rs.next()) { // 可能有多行结果
    // 通过字段名获取数据
    int id  = rs.getInt("id");
    String name = rs.getString("name");
}
```

- 4.关闭连接

```java
// 从后往前
rs.close();
stmt.close();
conn.close();
```

示例：

```java
import java.sql.*;
 
public class javaSQL {
    // MySQL 8.0 以上版本 - JDBC 驱动名及数据库 URL
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://hostname:3306/lottery?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
 
    // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "user";
    static final String PASS = "password";
 
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // 注册 JDBC 驱动
            Class.forName(JDBC_DRIVER);  // forName方法用于获取将指定的类实例化
        
            // 打开链接
            System.out.println("连接数据库...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
        
            // 执行查询
            System.out.println(" 实例化Statement对象...");
            stmt = conn.createStatement();
            String sql;
            sql = "SELECT * FROM lottery.Goods";
            ResultSet rs = stmt.executeQuery(sql);
        
            // 展开结果集数据库
            while (rs.next()) {
                // 通过字段检索
                int id  = rs.getInt("id");
                String name = rs.getString("price");
                String url = rs.getString("goodsName");
    
                // 输出数据
                System.out.print("id: " + id);
                System.out.print(", price: " + name);
                System.out.print(", goodsName: " + url);
                System.out.print("\n");
            }
            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        } catch(SQLException se) {
            // 处理 JDBC 错误
            se.printStackTrace();
        } catch(Exception e) {
            // 处理 Class.forName 错误
            e.printStackTrace();
        } finally {
            // 关闭资源
            try {
                if(stmt!=null) stmt.close();
            } catch(SQLException se2) {
            }// 什么都不做
            try {
                if(conn!=null) conn.close();
            } catch(SQLException se) {
                se.printStackTrace();
            }
        }
        System.out.println("Goodbye!");
    }
}
```

## MyBatis

MyBatis是一个Java中更高级的SQL框架，详细内容可以查看[官网](https://mybatis.org/mybatis-3/zh/index.html)