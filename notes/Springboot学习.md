# 新建一个项目

这里用的都是Maven

## jsp模板

- 1.通过Intellij IDEA创建项目

- 2.配置`application.properties`设置端口号和模板文件的前后缀，如：

```
server.port=8090
spring.mvc.view.prefix=/jsp/
spring.mvc.view.suffix=.jsp
```

指定了端口号为8090，模板文件位于`/src/main/webapp/jsp/`目录下，扩展名为`.jsp`

注意不要放在`WEN_INF`目录下

- 3.配置`pom.xml`，为jsp新增依赖

```xml
<dependency>
	<groupId>org.apache.tomcat.embed</groupId>
	<artifactId>tomcat-embed-jasper</artifactId>
</dependency>
<dependency>
	<groupId>javax.servlet</groupId>
	<artifactId>jstl</artifactId>
</dependency>
```

注意不要加上`<scope>provided</scope>`标签，因为provided表示只对编译和测试有效，实际运行无效，如果添加了provided，在使用Chrome访问时会直接下载文件

还要注意修改了pom.xml之后要`relode`一下maven

- 4.编写控制器程序

示例

```java
package com.springboot.demo.main;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class IndexController {

    @RequestMapping("/index")
    public String index() {
        return "index";
    }
}
```

- 5.编写jsp文件

示例

```xml
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Spring boot</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

- 6.修改运行文件Application

示例

```java
package com.springboot.demo.main;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}
}

```

运行Application.main就可以在浏览器输入`localhost:8090/index`来访问页面了

## Thymeleaf模板（推荐）

- 1.通过IDE创建项目

- 2.配置`application.properties`设置端口号

```
server.port=8090
```

- 3.配置`pom.xml`添加依赖

```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

注意reload

- 4.编写控制器程序

```java
package com.springboot.chapter2.main;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class IndexController {

    @RequestMapping("/index")
    public String index() {
        return "index";
    }
}
```

- 5.编写html模板文件

在`/src/main/recourses/tamplates`目录下新建`index.html`文件（需要`与控制器中return的视图名相同`）

```xml
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Spring boot</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

- 6.修改运行文件Application

```java
package com.springboot.demo.main;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}
}
```

然后在浏览器中访问`localhost:8090/index`就可以进入页面

可以看出，使用Thymeleaf要比jsp更简单


# IoC 控制反转

IoC（Inversion of Control）是Spring的两个核心理念之一

IoC是一种通过`描述`来生成或获取`对象`的技术，在Spring boot中通过`注解`的描述生成对象

Spring中每一个需要管理的对象称为`Spring Bean`（简称Bean），而管理这些Bean的容器称为`Spring IoC容器`（简称IoC容器）

IoC需要具备两个基本点功能：

- 1.通过描述管理Bean，包括发布和获取Bean
- 2.通过描述完成Bean之间的依赖关系

## 通过注解创建一个Bean并装配

首先创建一个Java简单对象（Plain Ordinary Java Object POJO）`User.java`作为Bean的源文件（文件位置为package名）

```java
package com.springboot.chapter3.pojo;

public class User {

    private Long id;
    private String userName;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }
}
```

然后定义一个Java配置文件`AppConfig.java`

```java
package com.springboot.chapter3.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.springboot.chapter3.pojo.User;

@Configuration
public class AppConfig {
    @Bean(name = "user")
    public User initUser() {
        User user = new User();
        user.setId(112L);
        user.setUserName("Chunar");
        return user;
    }
}
```

这里面`@Configuration`代表这是一个Java配置文件，Spring的容器会根据它来生成IoC容器取装配Bean

`@Bean`代表将initUser方法返回的POJO装配到IoC容器中，其属性name定义了这个Bean的名称

然后就可以使用`AnnotationConfigApplicationContext`来构建IoC容器：

```java
package com.springboot.chapter3.config;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import com.springboot.chapter3.pojo.User;

public class IoCTest {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(AppConfig.class);
        User user = ctx.getBean(User.class);
        System.out.println(user.getId() + " " + user.getUserName());
    }
}
```

注意，这里将AppConfig作为参数来构造了`AnnotationConfigApplicationContext`对象，通过`getBean`方法可以得到该POJO

运行IocTest.main()可以看到结果

## 通过扫描方式装配Bean

通过注解`@Component`和`@ComponentScan`可以将Bean由扫描的方式装配到容器中，从而不需要一个一个的使用`@Bean`来注入容器

`@Component`是标明`哪个类`被扫描进入Spring IoC容器，`@ComponentScan`是表明采用`何种策略`取扫描装配Bean

需要将上面的创建方式做一下修改：

```java
package com.springboot.chapter3.pojo;

import org.springframework.stereotype.Component;
import org.springframework.beans.factory.annotation.Value;

@Component("abcd")
public class User {

    @Value("11")
    private Long id;
    @Value("Qiuer")
    private String userName;
    ...
}
```

注意在类名上面添加了注解`@Component("abcd")`，abcd是自定义的Bean名

并且在每一个实例域上面添加了注解`@Value()`，它可以指定默认值，而不需在AppConfig中设置

然后AppConfig也需要相应的修改：

```java
package com.springboot.chapter3.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ComponentScan;


@Configuration
@ComponentScan(basePackages = "com.springboot.chapter3.*")
public class AppConfig {
}
```

只需在类名上添加一个`@ComponentScan`注解，而不需要在内部做任何的设置，程序将会自动扫描Bean

注意需要在@ComponentScan后指定扫描的路径，否则会默认在当前同名包内扫描

无需对`IoCTest`做任何修改，直接运行就能得到与上面相同的结果
