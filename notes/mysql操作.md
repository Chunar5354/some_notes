  * [安装](#%E5%AE%89%E8%A3%85)
    * [树莓派上](#%E6%A0%91%E8%8E%93%E6%B4%BE%E4%B8%8A)
    * [centos7](#centos7)
  * [配置](#%E9%85%8D%E7%BD%AE)
  * [远程登陆设置](#%E8%BF%9C%E7%A8%8B%E7%99%BB%E9%99%86%E8%AE%BE%E7%BD%AE)
    * [创建新用户并授权](#%E5%88%9B%E5%BB%BA%E6%96%B0%E7%94%A8%E6%88%B7%E5%B9%B6%E6%8E%88%E6%9D%83)
      * [1\.创建用户](#1%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7)
      * [2\.授权](#2%E6%8E%88%E6%9D%83)
      * [3\.撤销权限](#3%E6%92%A4%E9%94%80%E6%9D%83%E9%99%90)
      * [4\.删除用户](#4%E5%88%A0%E9%99%A4%E7%94%A8%E6%88%B7)
    * [修改远程连接配置文件](#%E4%BF%AE%E6%94%B9%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)
  * [常用命令](#%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)
    * [1\.新建](#1%E6%96%B0%E5%BB%BA)
    * [2\.为数据库添加数据](#2%E4%B8%BA%E6%95%B0%E6%8D%AE%E5%BA%93%E6%B7%BB%E5%8A%A0%E6%95%B0%E6%8D%AE)
    * [3\.修改数据库中的数据](#3%E4%BF%AE%E6%94%B9%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE)
    * [4\.从数据库中提取数据](#4%E4%BB%8E%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E6%8F%90%E5%8F%96%E6%95%B0%E6%8D%AE)
    * [5\.删除行](#5%E5%88%A0%E9%99%A4%E8%A1%8C)
    * [6\.为数据分组](#6%E4%B8%BA%E6%95%B0%E6%8D%AE%E5%88%86%E7%BB%84)
    * [7\.LIKE查找](#7like%E6%9F%A5%E6%89%BE)
    * [8\.JOIN方法将两个表关联起来](#8join%E6%96%B9%E6%B3%95%E5%B0%86%E4%B8%A4%E4%B8%AA%E8%A1%A8%E5%85%B3%E8%81%94%E8%B5%B7%E6%9D%A5)
    * [9\.AS方法](#9as%E6%96%B9%E6%B3%95)
    * [10\.日期计算](#10%E6%97%A5%E6%9C%9F%E8%AE%A1%E7%AE%97)
    * [11\.修改表中列的名称、类型](#11%E4%BF%AE%E6%94%B9%E8%A1%A8%E4%B8%AD%E5%88%97%E7%9A%84%E5%90%8D%E7%A7%B0%E7%B1%BB%E5%9E%8B)
    * [12\.插入新列](#12%E6%8F%92%E5%85%A5%E6%96%B0%E5%88%97)
      * [插入自增列](#%E6%8F%92%E5%85%A5%E8%87%AA%E5%A2%9E%E5%88%97)
    * [13\.查询前几行或后几行](#13%E6%9F%A5%E8%AF%A2%E5%89%8D%E5%87%A0%E8%A1%8C%E6%88%96%E5%90%8E%E5%87%A0%E8%A1%8C)
    * [14\.查看当前运行的命令](#14%E6%9F%A5%E7%9C%8B%E5%BD%93%E5%89%8D%E8%BF%90%E8%A1%8C%E7%9A%84%E5%91%BD%E4%BB%A4)
    * [15\.创建表时设置自增主键](#15%E5%88%9B%E5%BB%BA%E8%A1%A8%E6%97%B6%E8%AE%BE%E7%BD%AE%E8%87%AA%E5%A2%9E%E4%B8%BB%E9%94%AE)
    * [16\.创建表时使用外键](#16%E5%88%9B%E5%BB%BA%E8%A1%A8%E6%97%B6%E4%BD%BF%E7%94%A8%E5%A4%96%E9%94%AE)
    * [17\.远程连接mysql](#17%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5mysql)
  * [常见问题](#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)
    * [1\.中文字符](#1%E4%B8%AD%E6%96%87%E5%AD%97%E7%AC%A6)
    * [2\.忘记密码](#2%E5%BF%98%E8%AE%B0%E5%AF%86%E7%A0%81)
    * [3\.身份验证错误](#3%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E9%94%99%E8%AF%AF)
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
* [MySQL必知必会](#mysql%E5%BF%85%E7%9F%A5%E5%BF%85%E4%BC%9A)
  * [MySQL简介](#mysql%E7%AE%80%E4%BB%8B)
  * [查询SELECT](#%E6%9F%A5%E8%AF%A2select)
  * [通配符](#%E9%80%9A%E9%85%8D%E7%AC%A6)
  * [正则表达式](#%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F)
  * [计算字段](#%E8%AE%A1%E7%AE%97%E5%AD%97%E6%AE%B5)
    * [拼接](#%E6%8B%BC%E6%8E%A5)
    * [去掉空格](#%E5%8E%BB%E6%8E%89%E7%A9%BA%E6%A0%BC)
  * [分组](#%E5%88%86%E7%BB%84)
  * [联结表](#%E8%81%94%E7%BB%93%E8%A1%A8)
  * [组合查询](#%E7%BB%84%E5%90%88%E6%9F%A5%E8%AF%A2)
  * [全文本搜索](#%E5%85%A8%E6%96%87%E6%9C%AC%E6%90%9C%E7%B4%A2)
    * [进行全文本搜索](#%E8%BF%9B%E8%A1%8C%E5%85%A8%E6%96%87%E6%9C%AC%E6%90%9C%E7%B4%A2)
    * [查询扩展](#%E6%9F%A5%E8%AF%A2%E6%89%A9%E5%B1%95)
    * [布尔模式](#%E5%B8%83%E5%B0%94%E6%A8%A1%E5%BC%8F)


## 安装

### 树莓派上

- 安装：`sudo apt-get install mysql-server`
- 卸载：`sudo apt-ge autoremove --purge mysql-server`

### centos7

- 首先创建一个配置文件
```
# sudo vim /etc/yum.repos.d/MariaDB.repo
```

官方针对不同的系统给出了不同的配置文件内容，具体可以在[官网](https://downloads.mariadb.org/mariadb/repositories/)查看，比如centos7：
```
# MariaDB 10.4 CentOS repository list - created 2019-09-09 06:32 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.4/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

- 然后可以安装：
```
# sudo yum install MariaDB-server MariaDB-client -y
# sudo systemctl start mariadb.service       // 启动mysql
# sudo systemctl enable mariadb.service      // 设置开机自动启动
```

更换源之后如果提示安装包不存在，可以先执行`sudo yum clean all`再进行安装

之后进行安全性的配置：
```
# sudo mysql_secure_installation
```

输入命令之后根据提示进行配置就可以了

- 开放端口

centos由于有防火墙的存在，默认是无法远程连接mysql的，需要在firewalld中为mysql开放端口

首先查看当前firewalld的zones：
```
# sudo firewall-cmd --get-active-zones
```

结果中一般只有一个public，如果有其他的，需要为每一个zone都开放端口（将下面的public替换成对应的zone名称）：
```
# sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
# sudo firewall-cmd --reload         // 重启防火墙
```

- 卸载mysql

首先查看安装了哪些包：
```
# yum list installed mariadb*
```

把他们全部卸载掉：
```
# yum remove pkg_name
```

之后还要删除一些残留的文件

先查看这些文件是否存在：
```
# ls /etc/my.cnf
# ll /var/lib/mysql/
```

删除：
```
# rm -rf /etc/my.cnf
# rm -rf /var/lib/mysql/
```

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

比如：

```
grant all privileges on DBname.* to 'test_user'@'%' identified by 'pswd123' with grant option;
```

上面的语句为test_user用户在所有ip地址下经密码pswd123给DBname这个数据库的所有表授权了所有（all）权限
  
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
# sudo vi /etc/mysql/mariadb.conf.d/50-server.cnf
```
注释掉其中的`bind-address  = 127.0.0.1`这一行  
然后保存，重启


## 常用命令

参考[官方文档](https://dev.mysql.com/doc/refman/8.0/en/)

### 1.新建

- 可以使用

```
show databases;
```
查看已有数据库

- 对于已有的数据库，使用`use`命令进入该数据库（此命令可不加分号），比如：

```
use mysql
```

- 若想创建一个新的数据库，使用`create`命令:
```
create database your_table
```

- 进入数据库之后，使用
```
show tables;
```
查看表格

- 同样可以使用`create`命令来创建表格

```
create table your_table (column1 varchar(10), column2 varchar(20), column3 char(1), column4 date);
```
其中，`your_name`为创建的表格名称，`column`为列标签，后面带的参数表示这一列的数据类型和长度

- 使用`describe`命令查看表格的内容：

```
describe your_table;
```

### 2.为数据库添加数据

可以从文件中加载数据添加到数据库表格中

- 从文件：首先编辑一个`pet.txt`文件，各项之间用`tab`隔开，没有的值使用`\N`或者`NULL`代替，如：

```
Whistler        Gwen    bird    \N      1997-12-09      \N
```
注意这里面的各项要对应创建表格时候的各个列

然后使用load命令加载：

```sql
LOAD DATA LOCAL INFILE '/path/pet.txt' INTO TABLE pet
```

- 如果需要为表格增加新行，使用`insert`命令

```sql
INSERT INTO pet VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);
```
  
### 3.修改数据库中的数据

使用`update`命令

如：将name为Browser的宠物birth改为1989-08-31：

```sql
UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';
```

### 4.从数据库中提取数据

使用`select`命令，主要格式为：

```sql
SELECT 'what_to_select' // 选择哪一项数据，可以用 * 表示全部数据
FROM 'which_table' // 从哪一个表格
WHERE 'conditions_to_satisfy'; // 满足哪些条件
```

在`where`的条件判断中可以使用`and`和`or`等逻辑语句

- 选择数据并排序：
  - 使用`order`命令
  - 比如需要通过生日来排序，并只查看名字和生日两项:`SELECT name, birth FROM pet ORDER BY birth;`
  - 排序默认为升序，可以通过`desc`设置为降序：`SELECT name, birth FROM pet ORDER BY birth DESC;`
  
- `max()`函数寻找最大值

### 5.删除行

```sql
DELETE FROM tablename WHERE condition;
```

`tablename`为要操作的表，`condition`为删除的行所满足的条件

### 6.为数据分组

使用`group by`语句，将表中的行按照所选择的相同值来分组

### 7.LIKE查找

按`like 'b%' '%f' '%w%' `形式查找，也可以使用`_`下划线占位按长度查找

### 8.JOIN方法将两个表关联起来

- INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。（NATURAL JOIN）
- LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
- RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

### 9.AS方法

`AS`可以将一个一个元素暂时命名为另一个元素，而且不修改原来的元素
如`...TABLE pet AS p1 ...;`
或者`SELECT name as n1 FROM pet;`
  
### 10.日期计算

使用`TIMESTAMPDIFF()`命令，需要传递三个参数：

- 1.要计算的日期参数，可以是YEAR,MONTH,DAY等
- 2.减数
- 3.被减数
- 比如：`SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet;`
  - 其中`DURDATE()`是内置函数，返回当前日期
  - `AS`表示将其前面的内容（TIMESTAMPDIFF那一串）作为其后面的参数（age）显示在pet表格中
  
### 11.修改表中列的名称、类型

```sql
ALTER TABLE 'tablename'  MODIFY COLUMN 'column_name'  'new_name'  'new_type'    新默认值     新注释;  
ALTER TABLE   'table1'   MODIFY COLUMN   'column1'    'column2'  'float(4,2)'  DEFAULT NULL  COMMENT '注释';  // 示例
```

### 12.插入新列

```sql
ALTER TABLE 'tablename'
	ADD COLUMN 'colomnname' 'type' NOT NULL AFTER `columnname`;
```

在指定位置插入一列，`AFTER`后面指的是插入在那一列的后面

#### 插入自增列

插入名为`id`的自增列并将其设为主键（FIRST表示插入到第一列）

```sql
ALTER TABLE tablename ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST
```


### 13.查询前几行或后几行

使用`MILIT`语句，LIMIT后可以接受一个或两个整数参数：

```sql
SELECT * FROM table LIMIT 5;            // 查询前5行
SELECT * FROM table LIMIT 5, 10;        // 查询从第6行开始的10行（6-15）
SELECT * FROM table LIMIT 5, -1;        // 查询第6行到最后一行
```

可以通过加上`DESC`倒叙排列来查询后几行：

```sql
SELECT * FROM table WHERE id>$id ORDER BY id DESC LIMIT 5;     // 查询最后5行
```

### 14.查看当前运行的命令

```
show full processlist;
```

### 15.创建表时设置自增主键

```
CREATE TABLE table2 (
    ...
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ...
);
```

### 16.创建表时使用外键

假设已经有了table1，要将table2中的id2关联到table1中的id1上：

```
CREATE TABLE table2 (
    ...
    id2 INT,
    FOREIGN KEY(id) REFERENCES tabl1(id1),
    ...
);
```

### 17.远程连接mysql

通常mysql默认是关闭远程连接功能的，需要编辑配置文件开启

对于Debian系统的MariaDB，可以编辑`/etc/mysql/mariadb.cnf`，添加：

```
[mysqld]
bind-address = 0.0.0.0
```

然后重启mysql

```
$ sudo systemclt restart mysql
```

同时要注意开启防火墙上的mysql端口，默认是`3306`

可以在另一台安装了mysql的机器上试验连接：

```
mysql -h 目标IP -P3306 -u 用户名 -p密码
```


## 常见问题

### 1.中文字符

有时为了在数据库中存储中文字符，需要在创建数据库的时候指定`字符集`

```
create database db_name default charset=utf8;
```

或者可以修改现有的表

```
alter table table_name convert to character set utf8;
```

### 2.忘记密码

这里针对MariaDB在Centos7系统上的情况，如果忘记root密码，可以首先修改配置文件`vim /etc/my.cnf`

在其中添加

```
[mysqld]
skip-grant-tables
```

这样就能在登录的时候跳过权限认证，然后重启MariaDB

```
# sudo systemctl restart mariadb
```

然后在命令行输入`mysql`进入mysql

可能会遇到`The MariaDB server is running with the --skip-grant-tables option so it cannot execute this statement`这个问题，其实这里可以不用跳过权限验证，如果有其他用户的话用其他用户进行登录也是可以修改root的密码的

首先刷新权限
```
MaiaDB [(none)]> FLUSH PRIVILEGES;
```

设置新密码

```
MaiaDB [(none)]> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

然后再刷新权限

```
MaiaDB [(none)]> FLUSH PRIVILEGES;
```

这样新的root密码就修改好了

### 3.身份验证错误

在Django中使用MySQL时可能会出现`plugin caching_sha2_password could not be loaded`错误

是因为新版本的MySQL默认使用caching_sha2_password作为身份验证插件，旧版本是mysql_native_password，此时需要换回旧版插件

进入MySQL客户端：

```
ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
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

```sql
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


# MySQL必知必会

SQL(Structured Query Language，结构化查询语言)，是专门用来与数据库通信的语言

## MySQL简介

对于数据库的所有操作都是通过`DBMS`（数据库管理系统）完成的，MySQL就是一种DBMS

DBMS可分为两类：基于`共享文件系统`的DBMS和基于`客户机-服务器`的DBMS，前者常用于较低端的桌面用途

MySQL，Oracle等数据库是基于客户机-服务器的数据库，服务器部分是负责所有数据访问和处理的一个`软件`，且只有服务器软件与数据文件打交道；客户机是与`用户`打交道的软件

## 查询SELECT

- WHERE后可以添加BETWEEN...AND语句来实现范围查找，如

```sql
SELECT name FROM table1 WHERE id BETWEEN 1 and 10;
```

- 查找NULL值的时候需要使用`IS NULL`来匹配，而不是等号

- 在WHERE种，AND操作符的优先级比OR高

## 通配符

通配符必须跟在`LIKE`关键字之后，它可以指示MySQL使用通配符匹配而不是直接相等匹配

- `%` 表示任意字符出现`任意次数`

```sql
... WHERE name LIKE 'abc%';
```

搜索以abc开头的内容，%表示任意字符串

- `_` 表示`单个的`任意字符

## 正则表达式

MySQL中的正则表达式只是正则表达式的一个子集

需要使用关键字`REGEXP`

- 正则表达式中的匹配是包含匹配，而不是相等匹配，即`REGEXE '123'`会匹配到所有包含'123'的字符串

- OR操作：`'123|456'`会匹配包含'123'或'465'的字符串

- `[]`可以匹配括号中的字符之一，`'[123]'`可以匹配到1、2或3

- 如果要否定一个字符集，可以在括号里面的开始处加上`^`，即`'[^123]'`可以匹配除了1、2或3之外的任意字符

- 可以使用`-`来指定匹配范围，如`'[1-9]'`匹配1到9的数字，而`'[a-z]'`匹配任意字母

- 通过`\\`来将特殊字符转义

- 通过`*`指定任意多个字符的匹配，如`'s*'`可以匹配任意多个s（包括0个），`+`表示一个或多个，`?`表示0个或1个，还可以通过`{n, m}`来指定范围

- 通过`^`来定位在文本的`开始`（注意不要放在括号里，那就变成了否定），通过`$`来定位文本的`结尾`（`'s$'`表示匹配以s结尾的字符串，注意是放在后面）

## 计算字段

在SELECT查找时对数据进行预处理

### 拼接

通过`Concat()`函数将多个字符串拼接在一起

```sql
SELECT Concat(id, ' - ', name) FROM table1;
```

输出的形式就是`id - name`的格式

### 去掉空格

`RTrim()`去掉右边的空格

`LTrim()`去掉左边的空格

## 分组

- `HAVING`类似于WHERE，对结果进行筛选，但HAVING作用于分组

## 联结表

- 1.可以通过WHERE子句来联结两个表，如：

```sql
SELECT id, name, prod_name 
    FROM vendors, products 
    WHERE id = vend_id 
    ORDER BY id;
```

这种方法称为`等值联结`

- 2.通过`INNER JOIN ... ON ...`关键字来实现`内部联结`

```sql
SELECT id, name, prod_name 
    FROM vendors INNER JOIN products 
    ON id = vend_id 
    ORDER BY id;
```

结果与上面相同

- `自联结`，为同一个表使用不同的`别名`

- `外联结`，与内部联结之检索出符合条件的结果不同，外联结可以检索出某个表中的全部行，通过`LEFT`和`RIGHT`关键字来指定

```sql
SELECT id, name, prod_name 
    FROM vendors LEFT OUTER JOIN products 
    ON id = vend_id 
    order by id;
```

上面的sql语句会检索出vendors中的所有行（LEFT），如果products中没有匹配的值，将其填充为NULL

## 组合查询

使用`UNION`关键字可以将多个SELECT查询的结果合并为单个结果集返回

```sql
SELECT id, name FROM vendors 
    WHERE id = 2 
UNION 
SELECT id, name FROM vendors 
    WHERE id = 1; 
```

它等价于使用多条WHERE子句

```sql
SELECT id, name FROM vendors 
    WHERE id = 2 AND id = 1;
```

UNION默认自动取消重复的行，如果想要保留重复行，可以使用`UNION ALL`关键字

## 全文本搜索

使用全文本搜索可以更高性能地查找匹配指定关键字的内容

要想使用全文本搜索，需要在创建表的时候指定，或者创建表之后添加全文本属性

- 创建时指定：

```sql
CREATE TABLE vendors
(
    id int(3),
    name varchar(15),
    PRIMARY KEY(id),
    FULLTEXT(name),
) ENGINE=MyISAM;
```

注意只有`MyISAM`引擎支持全文本搜索，InnoDB是不支持的

- 创建后修改：

```sql
ALTER TABLE vendors ADD FULLTEXT INDEX fulltext_article(name);
```

### 进行全文本搜索

通过`Match()...Against()`函数来执行

```sql
SELECT * FROM vendors WHERE Match(name) Against('Jack');
```

就会搜索出name列里面包含`Jack`这个词的所有行，而且会按照`匹配度`对结果进行`排序`

### 查询扩展

全文本搜索只能匹配包含指定关键字的行，而查询扩展能够找到与搜索内容相关，但不含指定关键字的其他行

查询扩展的机制是进行`两次扫描`，第一次使用全文本搜索找到匹配行，然后根据匹配行中的内容选择出一些`有用词`，然后再次根据有用词进行全文本搜索

查询扩展通过在Against函数中加上`WITH QUERY EXPANSION`关键词来实现

```sql
SELECT * FROM vendors WHERE Match(name) Against('Jack' WITH QUERY EXPANSION);
```

### 布尔模式

使用布尔模式，除了可以指定需要出现的词，还可以指定不希望出现的词

```sql
SELECT * FROM vendors WHERE Match(name) Against('Jack -Mary' IN BOOLEAN MODE);
```

上面的语句查找包含Jack但不包含Mary的结果

注意布尔模式可以用在`非全文本搜索`中，但是速度很慢


