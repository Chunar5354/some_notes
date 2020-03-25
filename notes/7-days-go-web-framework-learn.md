在网上偶然看到的一个项目，用Go语言自己写一个web框架，感觉这个项目对学习Go语言和web原理都有所帮助，就学着写了一些，
[原文地址](https://geektutu.com/post/gee.html)

# 一些Go的基本知识

##  1.自建package

在Go语言中，只要拥有相同的`package name`开头的所有文件都可以视为是同一package中，比如本项目中有一个`gee`文件夹：
```
/gee
  gee.go
  router.go
  context.go
  go.mod
```

那只要这三个文件.go文件包含相同的package声明：
```go
package gee
```

并且使用
```
# go mod init gee
```

在gee目录中生成了一个`go.mod`文件，那么这三个.go文件都视为gee这个模块，可以通过`import ("gee") `来导入

更神奇的是这三个.go文件可以直接访问互相的内容，比如在context.go中定义了一个`Context`结构体，并为其定义了`GET()`方法，那么在另外两个文件中
就可以直接通过`Context.GET()`来调用，就`好像这三个文件是一个文件`，只不过为了实现各自专门的功能而拆分成三个文件

##  2.重定向package

注意项目根目录中的`go.mod`文件：

```go
module example

go 1.14

require gee v0.0.0

replace gee => ./gee
```

前面两行是自动生成的，后面两行是自定义的，意思是导入一个gee模块，并指定其路径（v0.0.0对于自定义的模块来说似乎没什么用，但是必须要加上，否则build的时候会出错）


# 7天web框架

##  1.框架的基本结构

这个框架很简单，依赖于Go内置的`net/http`库，只有一个gee模块

它的主要功能由以下几个结构体对象实现：

### 1.Engine

Engine在`gee.go`文件中定义，最终要暴露给用户，用户可以通过它来添加路由规则，以及监听端口，运行整个项目

其结构为：
```go
type Engine struct {
  	router *router   // 一个指向router结构体的指针
	// 不加变量名，直接给一个指针，这样可以使得Engine和RouterGroup共用，
  	// 这样在调用*Engine的时候就相当于调用了*RouterGroup，可以直接访问*RouterGroup中的属性
  	*RouterGroup
  	// 路由分组的数组
	groups []*RouterGroup
}
```

### 2.RouterGroup

RouterGroup在`gee.go`中定义，用于实现路由分组

其结构为：
```go
type RouterGroup struct {
	prefix string    // 该路由分组的前缀，比如'/p/a'和'/p/b' 都有共同的前缀'/p'
	middlewares []HandlerFunc   // 中间件
	parent *RouterGroup   // 一个指向RouterGroup的指针，使得该对象能够嵌套使用
	engine *Engine   // 指向Engine，方便通过Engine来调用各种接口
}
```

### 3.Context

Context在`context.go`中定义，用于设置HTTP响应的内容

其结构为：
```go
type Context struct {
	Writer http.ResponseWriter   // http响应对象，通过它来写入http相应的内容
	Req *http.Request   // http请求对象，获取http请求
	Path string    // url路径
	Method string   // http请求的方法，如GET，POST等
	StatusCode int   // http响应状态码，如200，301等
	Params map[string]string   // 一个关于路由地址的map，用于处理包含:或*等通配符的url路径
}
```

### 4.node

node在`trie.go`中定义，用于生成路由trie树，管理子地址

其结构为：
```go
type node struct {
	pattern string     // 待匹配路由
	part string        // 路由的一部分，在两个//之间
	children []*node   // 子节点
	isWild bool        // 是否精确匹配, part以:或*开头的为true
}
```

### 5.router

router在`router`中定义，用于注册路由表

其结构为：
```go
type router struct {
	roots map[string]*node   // 请求方法到节点的映射，键为http请求方法名，如"GET"
	handlers map[string]HandlerFunc  // http请求到处理方法的映射，键的形式为 method-pattern, 如"GET-/index"
}
```


##  2.框架运行的逻辑

框架最简单的使用逻辑为：

- 1. 创建一个Engine对象
- 2. 通过Engine的相应方法注册路由表
- 3. 监听端口，开启http服务

可以用下面的图片表示：

<div align=center><img src="https://github.com/Chunar5354/some_notes/blob/master/images/register-router.png" width=80% height=80%/></div>

### 1.路由表注册

一个web应用最基本的是通过在浏览器输入一个地址，能够返回相应的页面内容，这就需要将url地址与处理函数对应起来，也就是`路由表`

比如在`main.go`中有这样一段代码：
```go
r.GET("/index", func(c *gee.Context) {
		c.HTML(http.StatusOK, "<h1>Hello Gee</h1>")
	})
```

它就执行了一个路由表注册的功能
