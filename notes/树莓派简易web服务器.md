搭建轻量级WEB服务器使用的是`nginx`+`sqlite`+`php7`，关于他们的详细介绍还是百度一下吧。

由于网上大部分是安装php5的，现在树莓派更新了之后不太适用了，找了好久才找到新的操作方法，大部分来源于`树莓派实验室`。

# 第一步：安装

需要安装nginx和php7.0:

>sudo apt-get update
sudo apt-get install nginx
sudo apt-get install php7.0-fpm php7.0-cli php7.0-curl php7.0-gd php7.0-mcrypt php7.0-cgi
sudo service nginx start
sudo service php7.0-fpm restart

安装成功的话在浏览器输入树莓派的ip地址就能看到nginx的页面。


# 第二步：配置

要配置nginx里面的default文件：

>sudo vi /etc/nginx/sites-available/default

将以下部分：

```
location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
```

替换为：

```
location / {
index  index.html index.htm index.php default.html default.htm default.php;
}

location ~\.php$ {
fastcgi_pass unix:/run/php/php7.0-fpm.sock;
#fastcgi_pass 127.0.0.1:9000;
fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
include fastcgi_params;
}
```

然后重启nginx：

>sudo service nginx restart

# 第三步：添加php文件

nginx的默认存储文件夹是`/var/www/html`

在里面新建`test.php`文件，比如：

```php
<?PHP
echo "phptest";
```
然后在浏览器输入树莓派ip地址就能看到自己的网页。

*——by 秦小炅 2018.9.10*
