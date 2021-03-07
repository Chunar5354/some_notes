# 用户

## 添加新用户

```
$ adduser username
```

然后按照提示设置密码与信息

## 为用户赋予管理权限

```
$ usermod -aG sudo username
```

可以切换到改用户进行测试：

```
$ su - username
$ sudo whoami
```

## 删除用户

只删除用户，不删除文件

```
$ sudo deluser username
```

删除用户目录

```
$ sudo deluser --remove-home username
```

# 安全

## 禁止root用户远程登陆

编辑`/etc/ssh/sshd_config`文件，将

```
PermitRootLogin yes
```

修改为

```
PermitRootLogin no
```

然=然后重启ssh服务

```
$ sudo service sshd restart
```

# 安装软件

## Python3

安装高版本的Python时，首先删除原来版本的Python3，先找到Python3的位置

```
$ whereis python3
```

把结果中带有python3的全部删除掉，比如

```
$ rm -rf /usr/bin/python3
```

然后下载安装包

```
$ wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz/
```

解压

```
$ xz -d Python-3.7.4.tar.xz
$ tar -xvf Python-3.7.4.tar
```

首先安装依赖

``` 
$ apt-get install gcc libc6-dev zlib1g zlib1g.dev
```

编译并安装

```
$ cd Python-3.7.4
$ ./configure --prefix=/usr/local/python3
$ make  //这一步会花费较长时间
$ sudo make install
```

最后把python3和pip3的目录添加到环境变量中

```
$ sudo ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
$ sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

测试一下

```
$ python3 -V
```

## mysql

在[这里](https://dev.mysql.com/downloads/repo/apt/)找到最新版本的mysql发行包,并下载

```
$ wget https://dev.mysql.com/downloads/repo/apt/mysql-apt-config_0.8.16-1_all.deb
```

安装mysql(mariadb)

```
$ sudo apt-get install mariadb-server mariadb-client
```

安装后默认root账户是没有密码的，可以进行设置

```
$ sudo mysql_secure_installation
```

## golang

[官网]()下载安装包

安装

```
$ rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.linux-amd64.tar.gz
```

设置环境变量，添加以下内容到`~/.bashrc`（GOPATH可以在需要的时候另行设置，只要制定了go/bin就可以运行go程序了）:

```
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
```

然后刷新一下

```
$ source ~/.bsahrc
```

测试

```
$ go version
```
