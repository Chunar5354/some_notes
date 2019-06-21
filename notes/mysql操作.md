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
  
## 简单操作

参考[官方文档](https://dev.mysql.com/doc/refman/8.0/en/entering-queries.html)

### 查看
