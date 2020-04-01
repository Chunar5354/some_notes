在网上偶然看到的一个项目，用Go语言自己写一个web框架，感觉这个项目对学习Go语言和web原理都有所帮助，就学着写了一些，
[原文地址](https://geektutu.com/post/gee.html)

# 一些Go的基本知识

## Ⅰ.自建package

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

## Ⅱ.重定向package

注意项目根目录中的`go.mod`文件：

```go
module example

go 1.14

require gee v0.0.0

replace gee => ./gee
```

前面两行是自动生成的，后面两行是自定义的，意思是导入一个gee模块，并指定其路径（v0.0.0对于自定义的模块来说似乎没什么用，但是必须要加上，否则build的时候会出错）


# 7天web框架

## Ⅰ.框架的基本结构

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
	// 两个关于中间件的属性
	handlers []HandlerFunc  // 中间件函数列表
	index int  //表示中间件进行的层级
	// 为了添加HTML功能，在Context中也加上一个Engine属性
	engine *Engine
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


## Ⅱ.框架运行的逻辑

框架最简单的使用逻辑为：

- 1.创建一个Engine对象
- 2.通过Engine的相应方法注册路由表
- 3.监听端口，开启http服务

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

将"index"这个地址及其所使用的方法"GET"映射到了第二个参数定义的的处理方法

### 2.获取页面内容

既然已经将路由地址对应的处理方法储存好了，那么当我们在浏览器输入url地址的时候，程序是怎样分析这个地址并最终找到处理方法，呈现内容的呢？

在`main.go`中有这样一段代码：
```go
r.Run(":9999")
```

是调用了`gee.go`中的`Run()`方法：
```go
func (engine *Engine) Run(addr string) (err error) {
	return http.ListenAndServe(addr, engine)
}
```

其中`ListenAndServe()`方法是http库中的方法，运行该方法就会监听对应的端口号，实现http服务。第一个参数是端口号，第二个参数必须要带有一个`ServeHTTP()`方法

所以需要为Engine结构体实现一个ServeHTTP()方法:
```go
func (engine *Engine) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	c := newContext(w, req)
	engine.router.handle(c)
}
```

而在ServerHTTP()中又调用了`router.handle()`方法：
```go
func (r *router) handle(c *Context) {
	n, params := r.getRoute(c.Method, c.Path)
	if n != nil {
		c.Params = params
		key := c.Method + "-" + n.pattern
		r.handlers[key](c)
	} else {
		c.String(http.StatusNotFound, "404 NOt FOUND: %s\n", c.Path)
	}
}
```

在router.handle()中，通过`GetRoute()`方法去路由表中查找当前Context对象中包含的方法名和URL路径对应的处理方法`HandlerFunc`，然后执行它

至此完成了路由地址到路由表中对应处理方法的运行逻辑

### 3.路由处理

#### 3.1 Trie树

路由地址一般都是以`前缀树`（Trie树）的形式来存储，如下图所示：

<div align=center><img src="https://github.com/Chunar5354/some_notes/blob/master/images/Trie-tree.png" width=80% height=80%/></div>

根据url地址一层一层的向下查找

而且这样也可以实现`动态路由`：通过设置某些通配符(如上面图片中的`:`)，可以将某一类路由映射到相同的方法

比如在上面的Trie树中，`/jcak/a`和`/lucy/a`都会匹配到`/:name/a`的内容，并且将name参数分别设置成jack和lucy

在gee框架中，为了实现Trie树，在`trie.go`中创建了一个`node`结构体，结构如下：
```go
type node struct {
	pattern string     // 待匹配路由
	part string        // 路由的一部分，在两个//之间
	children []*node   // 子节点
	isWild bool        // 是否精确匹配, part以:或*开头的为true
}
```

并创建了`insert()`和`search()`方法用来向Trie树中插入节点和在Trie树中查找结点

#### 3.2 路由分组

有时需要为某一类路由实现同样的方法，如：

以`/admin`开头的路由需要检测权限
以`/post`开头的路由匿名可访问

那么可以将路由进行分组，比如以`/post`前缀分组，`/post/a`和`/post/b`是该分组下的子分组。作用在/post分组上的中间件(middleware)，也都会作用在子分组，子分组还可以应用自己特有的中间件

为了实现路由分组，在`gee.go`中新创建了一个`RouterGroup`结构体，结构如下：
```go
type RouterGroup struct {
	prefix string    // 该路由分组的前缀，比如'/p/a'和'/p/b' 都有共同的前缀'/p'
	middlewares []HandlerFunc   // 中间件
	parent *RouterGroup   // 一个指向RouterGroup的指针，使得该对象能够嵌套使用
	engine *Engine   // 指向Engine，方便通过Engine来调用各种借口
}
```

如果不应用中间件的话，RouterGroup和Engine有着类似的功能，它们都实现了`addRoute()`和`GET()`以及`POST()`等注册路由的方法

注意`mian.go`中的这段代码：
```go
v1 := r.Group("/v1")
```

通过RouterGroup中的`Group()`方法创建了一个路由分组，Group()方法在`gee.go`中：
```go
func (group *RouterGroup) Group(prefix string) *RouterGroup {
	engine := group.engine
	// 创建一个新的RouterGroup对象，因为groups是engine的一个属性，所以所有的groups共用一个个engine
	newGroup := &RouterGroup{
		// 新RouterGroup对象的路由前缀要包含当前RouterGroup对象的路由前缀
		prefix: group.prefix + prefix,
		// 新的RouterGroup对象是当前Routergroup的一个子分组
		parent: group,
		engine: engine,
	}
	// 将当前的分组存储到Engine的groups属性中
	engine.groups = append(engine.groups, newGroup)
	return newGroup
}
```

新建了分组之后，就可以为当前的分组进行添加中间件、定制路由规则等操作，在`main.go`中：
```go
// 为v1分组添加一个中间件
v1.Use(onlyForV1())
{
	// 此时对v1分组的操作会自动加上 "/v1" 路由前缀
	v1.GET("/hello/:name", func(c *gee.Context) {
	c.String(http.StatusOK, "hello %s, you're at %s\n", c.Param("name"), c.Path)
	})
	v1.POST("/login", func(c *gee.Context) {
		c.JSON(http.StatusOK, gee.H{
			"username": c.PostForm("username"),
			"password": c.PostForm("password"),
		})
	})
}
```


### 中间件

中间件`middleware`是用户自定义的处理方法，用来嵌入到框架中

在Gee框架中，中间件的定义与路由映射的Handler一致，处理的输入是`Context`对象，并应用在`RouterGroup`对象上

注意`main.go`中的代码：
```go
r.Use(gee.Logger(), gee.Recovery())
```

该句代码的意思是将logger()这个中间件添加到当前的RouterGroup对象r中

User()方法在`gee.go`中
```go
// ...HandlerFunc表示可以收任意多个middlewares参数，类似Python中的*args解包
func (group *RouterGroup) Use(middlewares ...HandlerFunc) {
	// 将中间件添加到Group中
	group.middlewares = append(group.middlewares, middlewares...)
}
```

通过Use()方法将传入的logger()函数添加到了RouterGroup的`middlewares`属性中

因为设计中间件是要用来处理Context对象，所以还要讲中间件函数添加到`Context`的`handlers`属性中，这时要对`ServeHTTP()`方法做一些修改

在`gee.go`文件中:
```go
func (engine *Engine) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	var middlewares []HandlerFunc  // 这里不能用 :=
	for _, group := range engine.groups {
		// 通过url的前缀判断，将与当前url对应的RouterGroup中的中间件添加到Context的handlers中
		if strings.HasPrefix(req.URL.Path, group.prefix) {
			middlewares = append(middlewares, group.middlewares...)
		}
	}
	c := newContext(w, req)
	c.handlers = middlewares
	c.engine = engine
	engine.router.handle(c)
}
```

注意到最后又调用了`handle()`方法，在`router.go`中对handle()方法也作出了修改：
```go
func (r *router) handle(c *Context) {
	n, params := r.getRoute(c.Method, c.Path)  // 获得路由信息
	// 将router中储存的地址信息和路由处理函数都添加到Context中
	if n != nil {
		c.Params = params
		key := c.Method + "-" + n.pattern
		c.handlers = append(c.handlers, r.handlers[key])
		// r.handlers[key](c)  运行HandlerFunc不再由Router来完成，而是由添加了中间件和router中所有HandlerFunc的Context来完成
	} else {
		c.handlers = append(c.handlers, func(c *Context) {
			c.String(http.StatusNotFound, "404 NOt FOUND: %s\n", c.Path)
		})
	}
	c.Next()  // Next会执行从 c.index+1 开始的所有c.handlers中的方法
}
```

在handle()中只是将所有的处理方法添加到了Context的handlers属性中，并没有调用这些方法，调用方法是在`c.Nect()`中实现的，在`context.go`中：
```go
func (c *Context) Next() {
	c.index++
	s := len(c.handlers)
	// 调用从 c.index+1 开始直到handlers最后一个中间件函数
	for ; c.index < s; c.index++ {
		c.handlers[c.index](c)
	}
}
```

那为什么不直接在handle()中就直接调用这些方法呢？主要在于通过Next()方法和Context.index属性可以控制程序执行的顺序

注意在Context.handlers中添加方法的`顺序`为：先自定义中间件, 后路由表注册的处理方法

例如应用了中间件 A 和 B，和路由映射的 Handler，c.handlers是这样的[A, B, Handler]，c.index初始化为-1，A和B的结构分别为
```
func A(c *Context) {
    part1
    c.Next()
    part2
}
func B(c *Context) {
    part3
    c.Next()
    part4
}
```

这时调用c.Next()，执行流程为:
```
1. c.index++，c.index 变为 0
   0 < 3，调用 c.handlers[0]，即 A
2. 执行 part1，调用 c.Next()
   c.index++，c.index 变为 1
3. 1 < 3，调用 c.handlers[1]，即 B
4. 执行 part3，调用 c.Next()
   c.index++，c.index 变为 2
5. 2 < 3，调用 c.handlers[2]，即Handler
6. Handler 调用完毕，返回到 B 中的 part4，执行 part4
7. part4 执行完毕，返回到 A 中的 part2，执行 part2
8. part2 执行完毕，结束。
```

执行顺序为：`part1 -> part3 -> Handler -> part 4 -> part2`

至此实现了中间件函数的执行
