# 安装

## Windows

Windows系统安装JDK可以直接在[官方网站](https://www.oracle.com/java/technologies/javase-jdk14-downloads.html)下载`.exe`的安装包，
然后根据[官方文档](https://docs.oracle.com/en/java/javase/14/install/installation-jdk-microsoft-windows-platforms.html#GUID-DAF345BA-B3E7-4CF2-B87A-B6662D691840)的提示配置环境变量即可

## Linux

Linux系统同样需要下载对应版本的安装包，不过在使用wget方法下载是需要注意，Oracle上的资源在下载时需要进行验证，如果直接wget下载的话，只能下载到几KB的错误文件

即使带上下面的cookies参数：

```
wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
```

看似能够下载完整的文件，但在解压时还是会出现问题

所以最好是下载到自己的电脑上，再传给linux机器

然后可以解压安装包到指定的文件

```
# sudo mkdir /usr/local/jdk

# tar -zxvf  jdk-14.0.1_linux-x64_bin.tar.gz -C /usr/local/jdk
```

然后需要添加环境变量

打开`~/.bash_profile`文件，添加这样一句

```
export JAVA_HOME=/usr/local/jdk/jdk-14.0.1
```

并且将`/usr/local/jdk/jdk-14.0.1/bin`添加到PATH变量中

这样环境变量就配置好了，可以在命令行输入

```
# java --version
```

来进行验证
