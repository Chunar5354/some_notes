go语言学习

## 安装

下载源码包来进行安装，需要科学上网，[地址](https://golang.org/dl/)

### windows上

选择下载windows的msi安装文件，双击运行即可（甚至连环境变量都自动配置了）

### linux上

选择对应的源码包，arm（树莓派）或者amd，然后将其解压到`/usr/local`目录下：
```
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
```

然后是比较麻烦的一件事，配置环境变量：

go语言需要配置4个环境变量：GOROOT、GOPATH、GOBIN（可选）及 PATH 

- GOROOT：go源码的安装目录，即`usr/local/go`
- GOPATH：下载扩展包的默认安装路径，包含三个子目录：
  - src：存放源代码(比如：.go .c .h .s等)，下载的扩展包也在这里
  - pkg：编译时生成的中间文件（比如：.a）
  - bin：编译后生成的可执行文件（为了方便，可以把此目录加入到 $PATH 变量中，如果有多个gopath，那么使用${GOPATH//://bin:}/bin添加所有的bin目录
  - GOPATH可以有很多个目录，在windows系统中彼此以分号`;`隔开，linux系统中彼此以冒号`:`隔开
- GOBIN：go install编译存放路径，可以不设置，此时可执行文件将会放在GOPATH的bin目录中
- PATH：系统环境变量，最后要将GOROOT、GOBIN和GOPATH/bin都添加到PATH中

对于`树莓派`，要将这些环境变量添加到`~/.bashrc`文件中，也可以添加到`/etc/profile`中（`~/.bashrc`是针对单个用户，/etc/profile针对全局，考虑到安全性，
最好添加到`~/.bashrc`中），输入命令：`vi ~/.bashrc`，将下面几行内容添加到文件末尾：
```
export GOROOT=/usr/local/go
export GOPATH=~/goproject:~/go_test          // 这里创建了两个GOPATH，安装的扩展库都发给在goproject文件夹中，在go_test里面创建自己的项目
export PATH=$PATH:${GOPATH//://bin:}/bin
```

然后在终端输入命令：
```
source ~/.bashrc
```

至此，环境变量配置完成，可以输入`do version`命令进行测试，如果配置成功，则会打印go的版本信息

### gopm下载工具

go语言获取依赖包的`go get`，因为需要科学上网，有时候可能会无法下载

有一个安装go扩展包的工具gopm，支持国内网络，安装方式：
```
go get -u github.com/gpmgo/gopm
```

如果是按照上一节的目录配置的环境变量，此时可以在`~/goproject/bin`目录下看到gopm

之后就可以使用`gopm get -g`来代替`go get`

- 不采用-g参数，会把依赖包下载.vendor目录下面
- 采用-g 参数，可以把依赖包下载到GOPATH目录中
