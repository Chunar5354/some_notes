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


# 语法知识

Java是一门静态语言，而且同于一般的编译语言或解释型语言。它首先将源代码编译成`字节码`，再依赖各种不同平台上的`虚拟机`来解释执行字节码，从而具有`一次编写，到处运行`的跨平台特性。

编译器对`文件`操作，Java解释器加载`类`

## 类

一个类的基本组成：

- 实例域
- 构造器
- 方法

方法包含隐式参数`this`，类似Python的`self`，但不用在定义方法的时候显式给出


## 静态

### 静态域

在实例域定义的时候加上`static`

```java
private static String name="";
```

每个类`只有一个`，为所有该类的实例对象所共用，类似于Python的类变量。属于类而不属于任何对象实例

### 静态常量

在定义的时候加上`final`，常量不可被修改，所以将其作为公有（public）也没有影响

```java
public static final int n=1234;
```

### 静态方法

静态方法是一种`不能向对象`实施操作的方法，它没有隐式参数

静态方法`不能访问实例域`，但可以访问自身的`静态域`

最好使用`类名`，而不是对象来调用静态方法


## 方法参数

Java的参数调用总是`按值调用`，方法不能修改所传入的变量的内容

如果传入的参数是一个对象的引用，那么方法可以修改被引用的对象的状态，但不能够修改参数的值

```java
harry = new Employee();
doSomething(harry);
```

如上面的例子，harry是Employee类的一个对象引用，当通过doSomething()方法来处理harry时，harry所指向的对象状态可能会改变，但harry自身的值不变


## 重载

多个方法有相同的名字，不同的参数

编译器会根据方法`给出的参数类型`和`特定方法调用所使用的值类型`进行匹配来挑选出应该使用哪个方法

方法名+参数类型：方法的`签名`


## 多态

Java中对象变量是`多态`的，一个类变量可以引用该类本身的对象，也可以引用该类子类的对象

- 静态绑定：调用private、static、final方法或构造器的时候，编译器能够准确地知道应该调用哪个方法

- 动态绑定：调用public方法时，调用哪个方法依赖于方法的`签名`（方法名+参数列表）

    动态绑定时，`虚拟机`事先为每个类创建了一个`方法表`，其中列出了所有方法的签名和调用方法，其搜索是自下而上的（从子类到超类）

## final

不允许被扩展和继承的类称为final类

如果在类中的方法声明为final，那么这个方法不能被子类覆盖

## 强制类型转换

使用圆括号将转换后的类型括起来，比如：

```java
double x = 1.234;
int nx = (int) x;
```


## 4种访问修饰符

- 1.private 仅对本类可见
- 2.public 对所有类可见
- 3.protected 对本包和所有子类可见
- 4.默认，不需要修饰符 对本包可见

## Object超类

- equals方法

- hashcode方法

- toString方法

## ArrayList数组列表

类型化`<>`

泛型

## 接收多个参数

`...`省略号

## 枚举类

```java
public enum Size { SMALL, MEDIUM, LARGE, EXTRA_LARGE};
```

实际上Size是一个类，它继承了`Enum`类，具有四个实例，尽量不要构建新对象

## 反射

能够分析类能力的程序称为反射
