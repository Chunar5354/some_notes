起因是搞一个微信小程序，通过websocet从服务器获取数据，但是小程序只支持wss协议，需要为服务器配置SSl证书。

## 证书下载

使用的是阿里云服务器，配置了域名和DNS之后可以在阿里云上购买免费的SSL证书，
这一步可根据[官方教程](https://help.aliyun.com/document_detail/144488.html?spm=a2c4g.11186623.2.13.331847b9jG38UW#task-2345554)
进行，购买完成后选择对应服务器的证书下载

## 证书配置

主要还是根据[官方教程](https://help.aliyun.com/document_detail/98727.html?spm=a2c4g.11186623.2.17.6e0227e72ZGADI#concept-zsp-d1x-yfb)(我这里
用的是Apache服务器)

不过在配置的时候有一些比较容易出错的地方

### 安装mod_ssl模块

官方教程让我们在`conf/httpd.conf`文件中配置
```
LoadModule ssl_module modules/mod_ssl.so
```

但是通常这一句本来是没有的，因为没有安装mod_ssl模块，解决方法为：

- 1. 安装apache工具
```
# sudo yum install httpd-devel
```

- 2. 安装mod_ssl

首先使用`httpd -v`查看当前的apache版本，然后到[这里](http://archive.apache.org/dist/httpd/)找到对应的apache压缩文件下载（下面以2.4.6版本为例）
```
# wget http://archive.apache.org/dist/httpd/httpd-2.4.6.tar.gz
```

然后解压
```
# tar -zxvf httpd-2.4.6.tar.gz
```

然后进入到`httpd-2.4.6`文件夹，把`modules`文件夹下的`loggers`和`ssl`两个文件夹复制到apache的modules路径中，
对于centos系统是`/etc/httpd/modules/`

然后进入到`/etc/httpd/modules/ssl`，输入命令
```
# sudo apxs -i -c -a -D HAVE_OPENSSL=1 -I /usr/include/openssl -lcrypto -lssl -ldl *.c
```

此时在`conf/httpd.conf`中会自动出现
```
LoadModule ssl_module modules/mod_ssl.so
```

**注意**不要按照官方教程所说的添加`Include conf/extra/httpd-ssl.conf`这一行，因为本身配置文件中已经添加过了(`IncludeOptional conf.d/*.conf`)

- 3. 配置ssl.conf

首先安装
```
# sudo yum install mod_ssl openssl
```

这样在`/etc/httpd/conf.d`中出现了`ssl.conf`文件，然后按照官方教程的内容修改`ssl.conf`

- 4. 重启apache
```
# sudo systemctl restart httpd
```

这时在浏览器中输入`https://xxxx`应该可以看到配置成功了

## 端口代理

因为wss默认使用443端口，而传输数据的应用使用的是其他端口，所以需要代理转发

修改`conf.d/ssl.conf`

```
ServerName xxxx  # 在这一行后添加以下内容
# Proxy Config
SSLProxyEngine on
 
ProxyRequests Off
ProxyPass /wss ws://127.0.0.1:1234   # 改成自己的端口
ProxyPassReverse /wss ws://127.0.0.1:1234
```

然后重启apache

之后就可以在应用的客户端将原来的ws链接替换成wss链接：
```
ws://xxxxxx:1234
# 修改成
wss://xxxxxx/wss   #不要带端口
```
