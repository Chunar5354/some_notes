## 安装

- 树莓派上
  - `sudo apt-get install mysql-server`
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


## 创建数据库

- 首先可以使用`show databases;`命令查看已有数据库
- 对于已有的数据库，使用`use`命令进入该数据库，比如：`use mysql`（此命令可不加分号）
- 若想创建一个新的数据库，使用`create`命令:`create database your_name`
- 进入数据库之后，使用`show tables`命令查看表格
- 同样可以使用`create`命令来创建表格
  - `create table your_name (column1 varchar(10), column2 varchar(20), column3 char(1), column4 date)`
  - 其中，`your_name`为创建的表格名称，`column`为列标签，后面带的参数表示这一列的数据类型和长度
- 使用`describe`命令查看表格的内容：`describe your_name`

