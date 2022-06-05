## 创建项目

使用[IDEA](https://www.jetbrains.com/idea/)来编写Spring Boot项目比较方便

在IDEA中创建新项目选择`Spring Initiallizr`，根据需要勾选即可创建Spring项目

## 文件说明

IDEA会自动生成一些文件，其中比较重要的有：

- 1.pom.xml

`pom.xml`是项目的maven依赖文件，在需要使用一些功能时需要在这里添加依赖

- 2.src/main/java

`src/main/java`中是项目的java源码

- 3.src/main/sources

`src/main/sources`中包含静态文件`static`，`templates`以及项目配置文件`application.properties`

## 在Linux上运行Spring boot项目

将Spring Boot项目打包成`jar`包，在安装有Java的Linux系统上运行jar包即可

在IDEA中打包的方法：点击右侧`maven`按钮，双击其中的`package`，然后会在项目的`target`文件夹中生成一个`.jar`文件

[![O4FsYT.png](https://s1.ax1x.com/2022/05/17/O4FsYT.png)](https://imgtu.com/i/O4FsYT)

将该jar文件复制到Linux系统中，输入命令

```
$ java -jar xx.jar
```

即可运行项目

- 注意：在打包jar时，如果没有自己编写测试用例，需要将`src/test`目录下的java文件删除

## IDEA添加jar包依赖

在IDEA中添加jar包：

`File` -> `Project Structure` -> `Modules` -> `点击加号` -> `JARs or Directories` -> 选择路径导入本地jar包

[![XukQKO.png](https://s1.ax1x.com/2022/05/28/XukQKO.png)](https://imgtu.com/i/XukQKO)

## maven依赖的版本查询

可以在[这里](https://mvnrepository.com/)查到

## 创建多modules项目

在一个Spring项目中可以整合多个模块，每个模块有自己的主程序，能够独立运行，这样可以为一个项目赋予多种功能

在IDEA中的创建方法为:`右键项目根目录` -> `New` -> `Module`

[![XwP57Q.png](https://s1.ax1x.com/2022/06/05/XwP57Q.png)](https://imgtu.com/i/XwP57Q)

进入新键Module的选项框后选择最上方的`New Module`，IDEA会自动设置好父模块，只需要自己设置子模块名即可

[![XwPTts.png](https://s1.ax1x.com/2022/06/05/XwPTts.png)](https://imgtu.com/i/XwPTts)

新建成功后在父模块的`pom.xml`中会多出一段：

```xml
<modules>
    <module>test</module>
</modules>
```

证明子模块被父模块引用

### 关于parent标签

在实践过程中创建父模块时使用的是`Spring Initializr`，在pom.xml中自动生成的`<parent>`标签为：

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.7.0</version>
    <relativePath/> <!-- lookup parent from repository -->
</parent>
```

在子项目中的parent标签最好改成一样的，否则可能会出现模块间互相导入依赖时`找不到目标`的问题

### 子模块之间互相引用

不同子模块之间的对象可以互相引用，需要在`pom.xml`中配置

假设被引用的子模块为`test-origin`，引用方子模块为`test-target`

需要在`test-origin`的`pom.xml`中设置相关信息：

```xml
<groupId>org.testapi</groupId>
<artifactId>test-origin</artifactId>
<version>1.0-SNAPSHOT</version>
```

在`test-target`的`pom.xml`中就可以进行依赖导入：

```xml
<dependency>
    <groupId>org.testapi</groupId>
    <artifactId>test-origin</artifactId>
    <version>1.0-SNAPSHOT</version>
    <scope>compile</scope>
</dependency>
```

从而在test-target模块中使用test-origin定义的对象
