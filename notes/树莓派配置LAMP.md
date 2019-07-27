在树莓派3B+上通过`Apache` `MySQL` `PHP7`和`phpmyadmin`搭建轻量服务器

## 安装Apache

```
sudo apt-get install apache2
```
如果安装成功，在浏览器输入`树莓派IP`就能看到Apache的默认界面

Apache的一些命令：
```
service apache2 status      //查看状态
service apache2 start       //启动apache
service apache2 stop        //关闭apache
service apache2 restart     //重启apache
```

## 安装MySQL

```
sudo apt-get install mysql-server mysql-client
```

## 安装PHP7

```
sudo apt-get install php php7.0-mysql
```

## 安装phpmyadmin

```
sudo apt-get install phpmyadmin
```
安装时会弹出对话框
- 第一个选择`web server`的选项中选择`apache2`
- 第二个选择`Yes`
- 然后设置两次密码

之后可能会出现一个error，说是连接不上mysql，这个可以选择`ignore`

然后进行配置
```
sudo chmod 777 /var/www/html
sudo a2enmod rewrite
sudo ln -s /usr/share/phpmyadmin /var/www/html
```
配置完成后，就可以通过浏览器输入`树莓派IP/phpmyadmin`来进入phpmyadmin界面登录数据库
