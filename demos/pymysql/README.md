使用python中的pymysql模块操作mysql数据库
[参考文章](https://mp.weixin.qq.com/s/OM8U4rTJBm17Ey0nNxPCZg)

## 安装

- 树莓派上：`pip3 install pyMySQL`

## 主要方法

### connect()对象

使用示例：
```python
import pymysql

conn = pymysql.connect(host='localhost', 
                       user='root', 
                       port=3306, 
                       password='your_passwd',
                       database='test',
                       charset='utf8')
```

使用该方法与数据建立连接，各个参数：
- host：连接的mysql主机
- user：mysql用户
- port：连接的端口
- password：密码
- database：要连接的数据库
- charset：编码方式，默认为gb2312

connect()对象的方法：
- close()：关闭连接
- commit()：提交操作，只有提交了操作才会执行
- rollback()：放弃之前的操作
- cursor()：返回cursor对象，用于执行sql语句并返回结果

### cursor()对象

使用示例：
```python
import pymysql

conn = pymysql.connect(host='localhost', 
                       user='root', 
                       port=3306, 
                       password='your_passwd',
                       database='test',
                       charset='utf8')

cur = conn.cursor()

sql1 = "select * from pet where sex='f'"
count = cur.execute(sql1)
```

cursor()对象的方法：
- close()：关闭
- execute(sql[, parameters])：执行语句，返回受影响的行数
  - 可以在sql字符串后面带参数，修改具体操作的内容
- fetchone()：查询结果的第一行数据，返回一个元组
- next()：查询当前行的下一行
- fetchall()：查询数据的所有行，返回一个元组
- scroll(value[,mode])：将行指针移动到某个位置
  - value表示移动的行数
  - mode表示移动的方式，`relative`表示相对当前行移动多少行；`absolute`表示移动到绝对的行数位置
  

### 大量数据的插入操作

如果有大量数据需要存入数据库，可以使用pymysql.cursor中的`executemany()`方法，使用示例：

```python
sql = "INSERT INTO tablename(create_time, value) VALUES(%s, %s)"  # sql语句中要为datalist留出位置
datalist = [(create_time1, value1), (create_time1, value1), ...]  # datalist是一个要插入到数据库中的数据元组的列表（或元组）
count = cursor.executemany(sql, datalist)  # 插入数据，需要两个参数——sql语句和对应的数据元组列表
conn.commit()  # 提交执行命令
```

在数据量很大时，使用`executemany()`要比循环执行单次插入操作速度快得多
