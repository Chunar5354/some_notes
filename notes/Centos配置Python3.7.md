CentOs 系统默认安装了python2.7版本，使用python3需要自己手动安装配置，这篇主要是使用下载源码并编译的方式来进行配置

- 首先安装一系列的依赖包：
```
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel -y
```
其中`zlib-devel` `gcc` `make` `libffi-devel`这几个包比较重要，如果没装可能会编译错误

- 之后在官网下载源码包
```
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
```

- 对源码包进行解压以及解压缩
```
xz -d Python-3.7.4.tar.xz
tar -xvf Python-3.7.4.tar
```

- 然后进行编译
```
cd Python-3.7.4
./configure --prefix=/usr/local/python3.7 --enable-optimizations
make  //这一步会花费较长时间
sudo make install
```
`prefix`后面是预安装目录，可以自行设定
`enable-optimizations`是一个编译优化命令

- 最后把python3的目录添加到环境变量中
```
sudo ln -s /usr/local/python3.7/bin/python3.7 /usr/bin/python3
```

这时在命令行输入`python3`就能够进入到python3的解释器中，并能够看到python3的版本

- 在安装了python3之后，需要对yum进行重新配置，因为yum是基于python2工作的
```
vi /usr/bin/yum 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2 
vi /usr/libexec/urlgrabber-ext-down 
把 #! /usr/bin/python 修改为 #! /usr/bin/python2
```
