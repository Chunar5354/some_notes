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
- GOPATH：go的工作区，也是下载扩展包的默认安装路径，包含三个子目录：
  - src：存放源代码(比如：.go .c .h .s等)，下载的扩展包也在这里
  - pkg：编译时生成的中间文件（比如：.a）
  - bin：编译后生成的可执行文件（为了方便，可以把此目录加入到 $PATH 变量中，如果有多个gopath，那么使用${GOPATH//://bin:}/bin添加所有的bin目录
  - GOPATH可以有很多个目录，在windows系统中彼此以分号`;`隔开，linux系统中彼此以冒号`:`隔开，多个目录时下载的扩展包会放在第一个GOPATH中
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

## 基础语法学习

参考[go的官方教程](https://tour.golang.org/welcome/1)

### 学习过程中记录的知识点

## 运行本地go程序

运行go程序有两种方法：

- 1.直接运行`.go`的源码文件
```
go run filename.go
```

- 2.使用`build`命令编译，然后运行（这样会加快运行速度）

go build比较复杂，需要展开讨论一下

### 关于go build

该命令的功能就是将`.go`的源码编译成可执行文件，它对于文件目录结构有一些要求：

- 事先准备：GOPATH设置

我们将自定义的文件夹添加到GOPATH环境变量后，需要在该目录下创建三个文件夹：

```
go_path/         // GOPATH环境变量中的路径
    bin/         // 存放可执行文件（在未设置GOBIN的情况下）
    pkg/         // 存放代码包的归档文件（.a文件）
    src/         // 存放源码包
```

然后在`src`中创建源码包文件夹，比如`gostudy`

再在gotest中创建一个测试源码文件`go_study.go`（最好不要命名为name_test.go，因为`_test.go`有特殊意义）：
```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println("This is a test")
}
```

此时文件目录为：
```
src/
    gostudy/
        go_study.go
```

此时，在gostudy目录下可以直接运行`go run go_study.go`查看结果

也可以将其编译：`go build`，然后会发现该目录下多了一个gostudy可执行文件（注意这个文件名，是src目录下的源码包的名字，而不是.go源文件的名字），可以通过`./gostudy`运行该文件查看结果（顺便感受一下两种方法速度上的区别）

然后还可以再进一步的安装这个可执行文件：`go install`，执行该命令后整个文件路径变成了这样：
```
go_path/
    bin/
        gostudy
    pkg/
    src/
        gostudy/
            go_study.go

```

原来的可执行文件`gostudy`跑到`bin`文件夹里面去了（如果设置了GOBIN环境变量则会跑到GOBIN里面），这时可以去到bin中执行`./gostudy`得到一样的结果

### 总结一下

- 上面的`go build`方法只在当前源码包只有一个.go源文件的时候有效（实际使用中也最好这么做）
- go build后面可以带上指定的源码包（必须是包含在GOPATH/src目录下的），如`go build gostudy`，这一条命令可以运行在任何目录下，并在当前目录生成gostudy可执行文件，只要gostudy是包含在GOPATH/src文件夹就可以
- go build可以带一些参数，如图所示：

![wtf](https://github.com/Chunar5354/some_notes/tree/master/demos/go_study/pic/go_build.png)

## go 自定义扩展包导入

go中可以通过import来引入扩展包，调用其中的方法，如果是引入自定义的扩展包，需要满足一些要求：

- 1.对路径的要求，被引入的包必须包含在GOROOT或者GOPATH的src文件夹中
- 2.对被引用文件的要求，要在文件开头声明源码包文件夹的名称

示例：

假设在当前某一GOPATH文件夹下的目录结构为：
```
go_path/
    bin/
    pkg/
    src/
        import_test/
            imt.go
```

`imt.go`的内容为：
```go
package import_test    // 注意这里是文件夹的名称

import ("fmt")

func Say() {           // 方法名称首字母大写
    fmt.Println("This is a test")
}
```

那么想要引用`src/import_test/imt.go`中的Say()函数，方法为：
```go
package main

import ("import_test")          // 引用的也是源码包文件夹的名字

func main() {
    import_test.Say()           // 直接调用函数Say()，事实上和文件名imt.go没啥关系
}
```

