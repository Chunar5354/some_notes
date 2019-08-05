* [安装](#%E5%AE%89%E8%A3%85)
* [配置](#%E9%85%8D%E7%BD%AE)
* [远程登陆设置](#%E8%BF%9C%E7%A8%8B%E7%99%BB%E9%99%86%E8%AE%BE%E7%BD%AE)
  * [创建新用户并授权](#%E5%88%9B%E5%BB%BA%E6%96%B0%E7%94%A8%E6%88%B7%E5%B9%B6%E6%8E%88%E6%9D%83)
    * [1\.创建用户](#1%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7)
    * [2\.授权](#2%E6%8E%88%E6%9D%83)
    * [3\.撤销权限](#3%E6%92%A4%E9%94%80%E6%9D%83%E9%99%90)
    * [4\.删除用户](#4%E5%88%A0%E9%99%A4%E7%94%A8%E6%88%B7)
  * [修改远程连接配置文件](#%E4%BF%AE%E6%94%B9%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
* [常用命令](#%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)
  * [1\.为数据库添加数据](#1%E4%B8%BA%E6%95%B0%E6%8D%AE%E5%BA%93%E6%B7%BB%E5%8A%A0%E6%95%B0%E6%8D%AE)
  * [2\.修改数据库中的数据](#2%E4%BF%AE%E6%94%B9%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE)
  * [3\.从数据库中提取数据](#3%E4%BB%8E%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E6%8F%90%E5%8F%96%E6%95%B0%E6%8D%AE)
  * [4\.为数据分组](#4%E4%B8%BA%E6%95%B0%E6%8D%AE%E5%88%86%E7%BB%84)
  * [5\.LIKE查找](#5like%E6%9F%A5%E6%89%BE)
  * [6\.JOIN方法将两个表关联起来](#6join%E6%96%B9%E6%B3%95%E5%B0%86%E4%B8%A4%E4%B8%AA%E8%A1%A8%E5%85%B3%E8%81%94%E8%B5%B7%E6%9D%A5)
  * [7\.AS方法](#7as%E6%96%B9%E6%B3%95)
  * [8\.日期计算](#8%E6%97%A5%E6%9C%9F%E8%AE%A1%E7%AE%97)
* [MYSQL中的索引](#mysql%E4%B8%AD%E7%9A%84%E7%B4%A2%E5%BC%95)
  * [1\.创建INDEX索引](#1%E5%88%9B%E5%BB%BAindex%E7%B4%A2%E5%BC%95)
  * [2\.主键](#2%E4%B8%BB%E9%94%AE)
  * [3\.在创建表时创建索引](#3%E5%9C%A8%E5%88%9B%E5%BB%BA%E8%A1%A8%E6%97%B6%E5%88%9B%E5%BB%BA%E7%B4%A2%E5%BC%95)
* [EXPLAIN方法](#explain%E6%96%B9%E6%B3%95)
* [从文件中调用SQL命令](#%E4%BB%8E%E6%96%87%E4%BB%B6%E4%B8%AD%E8%B0%83%E7%94%A8sql%E5%91%BD%E4%BB%A4)
  * [在命令行中使用：](#%E5%9C%A8%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%B8%AD%E4%BD%BF%E7%94%A8)
  * [在mysql中使用：](#%E5%9C%A8mysql%E4%B8%AD%E4%BD%BF%E7%94%A8)
* [规范化](#%E8%A7%84%E8%8C%83%E5%8C%96)
  * [第一范式](#%E7%AC%AC%E4%B8%80%E8%8C%83%E5%BC%8F)
  * [第二范式](#%E7%AC%AC%E4%BA%8C%E8%8C%83%E5%BC%8F)
  * [第三范式](#%E7%AC%AC%E4%B8%89%E8%8C%83%E5%BC%8F)
* [事务](#%E4%BA%8B%E5%8A%A1)
* [备份及恢复](#%E5%A4%87%E4%BB%BD%E5%8F%8A%E6%81%A2%E5%A4%8D)


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

#### 1.创建用户
```
create user 'username'@'host' identified by 'password'
```
- 其中`username`表示新建用户的用户名
- `host`表示可以在那些主机可以登录，可以指定主机的ip，如果要设置所有主机可登录，将`host`替换为`%`
- `password`表示该用户登录的密码
  
#### 2.授权

新建的用户是没有数据库的操作权限的，需要为其授权：

```
grant privileges on databasename.tablename to 'username'@'host'
```
- 其中`privileges`表示具体赋予哪一项权限，如`update` `delete`等，如果要赋予所有操作权限，将`privileges`替换成`all`
- `databasename`表示该权限是针对哪一个数据库，如果对于所有数据库都赋予该权限，将`databasename`替换成`*`
- `tablename`表示权限针对哪一个表格，如果对于所有表格都赋予该权限，将`tablename`替换成`*`
- 注意二者之间的`.`不要落下
- `username`和`host`意义与上面一样
  
#### 3.撤销权限
```
revoke privileges on databasename.tablename to 'username'@'host'
```
各参数的意义与上面相同

#### 4.删除用户
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

## 常用命令

参考[官方文档](https://dev.mysql.com/doc/refman/8.0/en/)

- 首先可以使用`show databases;`命令查看已有数据库
- 对于已有的数据库，使用`use`命令进入该数据库，比如：`use mysql`（此命令可不加分号）
- 若想创建一个新的数据库，使用`create`命令:`create database your_name`
- 进入数据库之后，使用`show tables`命令查看表格
- 同样可以使用`create`命令来创建表格
  - `create table your_name (column1 varchar(10), column2 varchar(20), column3 char(1), column4 date)`
  - 其中，`your_name`为创建的表格名称，`column`为列标签，后面带的参数表示这一列的数据类型和长度
- 使用`describe`命令查看表格的内容：`describe your_name`

### 1.为数据库添加数据

可以从文件中加载数据添加到数据库表格中

- 从文件：首先编辑一个`pet.txt`文件，各项之间用`tab`隔开，没有的值使用`\N`或者`NULL`代替
  - 如：`Whistler        Gwen    bird    \N      1997-12-09      \N`
  - 注意这里面的各项要对应创建表格时候的各个列
  - 使用load命令加载：`LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet`
- 如果需要为表格增加新行，使用`insert`命令
  - `INSERT INTO pet VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);`
  
### 2.修改数据库中的数据

使用`update`命令

- 如：将name为Browser的宠物birth改为1989-08-31：`UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';`
  
### 3.从数据库中提取数据

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
  
- `max()`函数寻找最大值

### 4.为数据分组

使用`group by`语句，将表中的行按照所选择的相同值来分组

### 5.LIKE查找

按`like 'b%' '%f' '%w%' `形式查找，也可以使用`_`下划线占位按长度查找

### 6.JOIN方法将两个表关联起来

- INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。（NATURAL JOIN）
- LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
- RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

### 7.AS方法

`AS`可以将一个一个元素暂时命名为另一个元素，而且不修改原来的元素
如`...TABLE pet AS p1 ...;`
或者`SELECT name as n1 FROM pet;`
  
### 8.日期计算

使用`TIMESTAMPDIFF()`命令，需要传递三个参数：

- 1.要计算的日期参数，可以是YEAR,MONTH,DAY等
- 2.减数
- 3.被减数
- 比如：`SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet;`
  - 其中`DURDATE()`是内置函数，返回当前日期
  - `AS`表示将其前面的内容（TIMESTAMPDIFF那一串）作为其后面的参数（age）显示在pet表格中
  
### 9.修改表中列的名称、类型

```
ALTER TABLE tablename  MODIFY COLUMN column_name  new_name  new_type     新默认值     新注释;  
ALTER TABLE   table1   MODIFY COLUMN   column1    column2  float(4,2)  DEFAULT NULL  COMMENT '注释';  // 示例
```
  
## MYSQL中的索引

使用索引可以在大型数据库中减少数据搜索的时间

常用的索引有INDEX，PRIMARY KEY（主键），FULLTEXT

### 1.创建INDEX索引

通过ALTER创建：
```
ALTER TABLE pet ADD INDEX(name(10));
```

该命令的意义为为`name`列创建索引，长度为10个字符（索引中只存储10个字符）

*通过索引进行检索比较复杂，日后再续*

### 2.主键

主键是每行都不同的`唯一`值，使用逐渐可以唯一的检索到某一行，在关系型数据库中一个表的主键通常会作为另一个表的外键`foreign key`

通过ALTER创建：
```
ALTER TABLE pet ADD PRIMARY KEY(id(10));
```

意为将`id`列创建为主键，注意id必须每一行都是唯一值

创建了主键之后使用`DESCRIBE pet`会看到`Key`这一列会发生变化

### 3.在创建表时创建索引

```
CREATE TABLE classics (
author VARCHAR(128),
title VARCHAR(128),
category VARCHAR(16),
year SMALLINT,
isbn CHAR(13),
INDEX(author(20)),
INDEX(title(20)),
INDEX(category(4)),
INDEX(year),
PRIMARY KEY (isbn)) ENGINE MyISAM;
```
注意最后要设置储存引擎，一般为`MyISAM`

## EXPLAIN方法

使用EXPLAIN方法可以解释如何发出的查询并打印出来，只要在SELECT前面加上它就能实现

```
EXPLAIN SELECT* FROM pet;
```
使用它也可以查看查询是否通过索引来实现
  
## 从文件中调用SQL命令

对于一些重复使用的命令，可以将其保存在文件中调用

### 在命令行中使用：
```
shell> mysql -h host -u user -p < finename
Enter password: ********
```
- 可以加上参数`-t`来使输出的格式与直接在命令行输入SQL命令时的输出格式一致
- 可以加上参数`-v`来打印所运行的SQL命令

### 在mysql中使用：
有两种方法
```
mysql> source filename;
mysql> \. filename
```

## 规范化

将数据分开放入表中并创建主键的过程称为规范化，主要目的是保证每一条信息在数据库中只出现一次

有三种范式

*涉及到好多图表，先把概念记到这里*

### 第一范式

第一范式有三个要求：
- 不能有包含相同类型数据的重复列出现
- 所有的列都是单值
- 要有一个主键来标识每一行

### 第二范式

第二范式首先要求满足第一范式，并在第一范式的基础上`消除多行间的冗余`

### 第三范式

第三范式在第一、第二范式的基础上，要求`数据不直接依赖于主键`

使用第三范式通常会增加表的数量，一般不需要使用

## 事务

使用MYSQL中的事务功能可以撤销一些操作，使用方法：
```
BEGIN;
UPDATE .... ;
INSERT .... ;
COMMIT;
```

在`BEGIN`之后的操作都是暂时性的，直到通过`COMMIT`提交之前他们都是可撤回的

撤回操作使用`ROLLBACK`
```
BEGIN;
UPDATE .... ;
INSERT .... ;
ROLLBACK;
```
这样UPDATE和INSERT操作就被撤回了

## 备份及恢复

使用`mysqldump`命令可以将数据库进行备份（在命令行下）

在备份之前最好将要备份的数据库加锁`LOCK`，或者确定备份过程中不会有用户向表中写入数据

```
LOCK TABLES .... ;
```
备份之后用`UNLOCK`解锁
```
UNLOCK TABLES;
```

mysqldump命令的使用方法：
```
mysqldump -u user -ppassword database
// database为要备份的数据库
```

直接运行该命令会将备份的内容打印在屏幕上，也可以将这些数据保存到文件中，使用`>`符号：
```
mysqldump -u user -ppassword database > database.sql
```

然后可以查看该文件，其中的内容包含所有重新创建表的命令和重新填充它们的数据

从备份文件中恢复数据库，使用`<`符号：
```
mysqldump -u user -ppassword -D database < database.sql
// -D表示恢复单个数据库
```


