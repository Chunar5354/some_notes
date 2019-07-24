## CentOS系统的配置

主要是针对CentOS系统的初始配置，如果已经配置好可以跳过

- 首先更新一下系统
```
sudo yum update
```

- 安装[EPEL](https://fedoraproject.org/wiki/EPEL)仓库(方便资源安装)
```
sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

- 安装[Remi's RPM](https://rpms.remirepo.net/)仓库
```
sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

- 查看一下仓库是否成功安装
```
sudo yum repolist
```

- 安装yum-utils包
```
sudo yum install yum-utils -y
```

## CentOS的防火墙操作

CentOS自带`fierwalld`，在进行网络应用端口等配置的时候常常会用到，关于它的一些操作：

- 启动防火墙
```
systemctl start firewalld 
```

- 关闭防火墙
```
systemctl stop firewalld 
```

- 设置防火墙开机启动
```
systemctl enable firewalld
```

- 停止防火墙并禁止开机启动
```
sytemctl disable firewalld 
```

- 重启防火墙
```
firewall-cmd --reload
```

- 查看防火墙状态
```
systemctl status firewalld
or >> firewall-cmd --state
```

- 查看区域信息
```
firewall-cmd --get-active-zones
```

- 查看所有信息
```
sudo firewall-cmd --list-all
```

- 添加许可服务
将`name`替换成要添加的服务名称
```
sudo firewall-cmd --add-service=name --permanent
```

- 添加端口
将`port_number`替换成端口数字，后面是相应的协议
```
sudo firewall-cmd --add-port=port_number/tcp --permanent
```


## 在CentOS上安装Python3

CentOS 系统默认安装了python2.7版本，使用python3需要自己手动安装配置，这篇主要是使用下载源码并编译的方式来进行配置

- 首先安装一系列的依赖包：
```
sudo yum install wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel -y
```
其中`zlib-devel` `wget` `gcc` `make` `libffi-devel`这几个包比较重要，如果没装可能会编译错误

- 之后在官网下载源码包
```
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
```

- 对源码包进行解压以及解压缩
```
- xz -d Python-3.7.4.tar.xz
- tar -xvf Python-3.7.4.tar
```

- 然后进行编译
```
- cd Python-3.7.4
- ./configure --prefix=/usr/local/python3
- make  //这一步会花费较长时间
- sudo make install
```
`prefix`后面是预安装目录，可以自行设定

- 最后把python3和pip3的目录添加到环境变量中
```
sudo ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

这时在命令行输入`python3`就能够进入到python3的解释器中，并能够看到python3的版本
并可以使用pip3进行相关包的安装

- 在安装了python3之后，需要对yum进行重新配置，因为yum是基于python2工作的
```
- vi /usr/bin/yum 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2 
- vi /usr/libexec/urlgrabber-ext-down 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2
```
