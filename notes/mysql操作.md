## 安装

- 树莓派上
  - 安装：`sudo apt-get install mysql-server`
  - 卸载：`sudo apt-ge autoremove --purge mysql-server`
- windows

## 配置

- 设置密码
树莓派上安装mysql默认是没有密码的，需要自己添加
  - 首先空密码登陆`sudo mysql -u root`
  - 设置root账户密码
  ```
  use mysql;
  update user set plugin='mysql_native_password' where user='root';
  UPDATE user SET password=PASSWORD('你自己的密码') WHERE user='root';
  flush privileges;
  exit;
  ```
  - 注意每一条mysql的命令都需要以`;`为结尾
  - 设置成功后就可以通过密码登陆`sudo mysql -h localhost -u root -p`，-h表示host，-u表示user，后面要带参数，-p表示password密码登陆
  
## 远程登陆设置

### 创建新用户并授权

#### 创建用户
```
create user 'username'@'host' identified by 'password'
```
- 其中`username`表示新建用户的用户名
- `host`表示可以在那些主机可以登录，可以指定主机的ip，如果要设置所有主机可登录，将`host`替换为`%`
- `password`表示该用户登录的密码
  
#### 授权

新建的用户是没有数据库的操作权限的，需要为其授权：

```
grant privileges on databasename.tablename to 'username'@'host'
```
- 其中`privileges`表示具体赋予哪一项权限，如`update` `delete`等，如果要赋予所有操作权限，将`privileges`替换成`all`
- `databasename`表示该权限是针对哪一个数据库，如果对于所有数据库都赋予该权限，将`databasename`替换成`*`
- `tablename`表示权限针对哪一个表格，如果对于所有表格都赋予该权限，将`tablename`替换成`*`
- 注意二者之间的`.`不要落下
- `username`和`host`意义与上面一样
  
#### 撤销权限
```
revoke privileges on databasename.tablename to 'username'@'host'
```
各参数的意义与上面相同

#### 删除用户
```
drop user 'username'@'host'
```

### 修改远程连接配置文件

- 对于树莓派
修改配置文件
```
sudo vi /etc/mysql/mariadb.conf.d/50-server.cnf
```
注释掉其中的`bind-address  = 127.0.0.1`这一行  
然后保存，重启

## 创建数据库

参考[官方文档](https://dev.mysql.com/doc/refman/8.0/en/)

- 首先可以使用`show databases;`命令查看已有数据库
- 对于已有的数据库，使用`use`命令进入该数据库，比如：`use mysql`（此命令可不加分号）
- 若想创建一个新的数据库，使用`create`命令:`create database your_name`
- 进入数据库之后，使用`show tables`命令查看表格
- 同样可以使用`create`命令来创建表格
  - `create table your_name (column1 varchar(10), column2 varchar(20), column3 char(1), column4 date)`
  - 其中，`your_name`为创建的表格名称，`column`为列标签，后面带的参数表示这一列的数据类型和长度
- 使用`describe`命令查看表格的内容：`describe your_name`

### 为数据库添加数据

可以从文件中加载数据添加到数据库表格中

- 从文件：首先编辑一个`pet.txt`文件，各项之间用`tab`隔开，没有的值使用`\N`或者`NULL`代替
  - 如：`Whistler        Gwen    bird    \N      1997-12-09      \N`
  - 注意这里面的各项要对应创建表格时候的各个列
  - 使用load命令加载：`LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet`
- 如果需要为表格增加新行，使用`insert`命令
  - `INSERT INTO pet VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);`
  
### 修改数据库中的数据

使用`update`命令

- 如：将name为Browser的宠物birth改为1989-08-31：`UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';`
  
### 从数据库中提取数据

使用`select`命令，主要格式为：
```
SELECT what_to_select // 选择哪一项数据，可以用 * 表示全部数据
FROM which_table // 从哪一个表格
WHERE conditions_to_satisfy; // 满足哪些条件
```

在`where`的条件判断中可以使用`and`和`or`等逻辑语句

- 选择数据并排序：
  - 使用`order`命令
  - 比如需要通过生日来排序，并只查看名字和生日两项:`SELECT name, birth FROM pet ORDER BY birth;`
  - 排序默认为升序，可以通过`desc`设置为降序：`SELECT name, birth FROM pet ORDER BY birth DESC;`
  
### 日期计算

使用`TIMESTAMPDIFF()`命令，需要传递三个参数：

- 1.要计算的日期参数，可以是YEAR,MONTH,DAY等
- 2.减数
- 3.被减数
- 比如：`SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet;`
  - 其中`DURDATE()`是内置函数，返回当前日期
  - `AS`表示将其前面的内容（TIMESTAMPDIFF那一串）作为其后面的参数（age）显示在pet表格中
