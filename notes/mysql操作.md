## 安装

- 树莓派上
  - 安装：`sudo apt-get install mysql-server`
  - 卸载：`sudo apt-ge autoremove --purge mysql-server`
- windows

## 配置sp

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
