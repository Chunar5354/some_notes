在网上偶然看到的一个项目，用Go语言自己写一个web框架，感觉这个项目对学习Go语言和web原理都有所帮助，就学着写了一些，
[原文地址](https://geektutu.com/post/gee.html)


* [一些Go的基本知识](#%E4%B8%80%E4%BA%9Bgo%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%9F%A5%E8%AF%86)
  * [Ⅰ\.自建package](#%E2%85%B0%E8%87%AA%E5%BB%BApackage)
  * [Ⅱ\.重定向package](#%E2%85%B1%E9%87%8D%E5%AE%9A%E5%90%91package)
  * [Ⅲ\.异常处理](#%E2%85%B2%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)
    * [主动抛出异常panic](#%E4%B8%BB%E5%8A%A8%E6%8A%9B%E5%87%BA%E5%BC%82%E5%B8%B8panic)
    * [defer](#defer)
    * [recover](#recover)
* [7天web框架](#7%E5%A4%A9web%E6%A1%86%E6%9E%B6)
  * [Ⅰ\.框架的基本结构](#%E2%85%B0%E6%A1%86%E6%9E%B6%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84)
    * [1\.Engine](#1engine)
    * [2\.RouterGroup](#2routergroup)
    * [3\.Context](#3context)
    * [4\.node](#4node)
    * [5\.router](#5router)
  * [Ⅱ\.框架运行的逻辑](#%E2%85%B1%E6%A1%86%E6%9E%B6%E8%BF%90%E8%A1%8C%E7%9A%84%E9%80%BB%E8%BE%91)
    * [1\.路由表注册](#1%E8%B7%AF%E7%94%B1%E8%A1%A8%E6%B3%A8%E5%86%8C)
    * [2\.获取页面内容](#2%E8%8E%B7%E5%8F%96%E9%A1%B5%E9%9D%A2%E5%86%85%E5%AE%B9)
    * [3\.路由处理](#3%E8%B7%AF%E7%94%B1%E5%A4%84%E7%90%86)
      * [3\.1 Trie树](#31-trie%E6%A0%91)
      * [3\.2 路由分组](#32-%E8%B7%AF%E7%94%B1%E5%88%86%E7%BB%84)
    * [4\.中间件](#4%E4%B8%AD%E9%97%B4%E4%BB%B6)
    * [5\.模板和静态文件](#5%E6%A8%A1%E6%9D%BF%E5%92%8C%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6)
      * [加载HTML模板](#%E5%8A%A0%E8%BD%BDhtml%E6%A8%A1%E6%9D%BF)
      * [模板渲染（定制函数）](#%E6%A8%A1%E6%9D%BF%E6%B8%B2%E6%9F%93%E5%AE%9A%E5%88%B6%E5%87%BD%E6%95%B0)
      * [静态文件](#%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6)


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

## Ⅲ.异常处理

### 主动抛出异常panic

与Python语言进行类比，Go中也有主动抛出异常的命令`panic`，用法：
```go
func main() {
	fmt.Println("before panic")
	panic("crash")
	fmt.Println("after panic")
}
```

运行结果：
```
before panic
panic: crash

goroutine 1 [running]:
main.main()
        /main.go:7 +0x9c
exit status 2
```

可见程序运行到panic处捕获了一个异常，当前线程在此处停止

### defer

Go中的`defer`命令有点类似Python中的`try...finally...`，即无论是否发生异常，defer中的命令总要运行，并且在出现异常处`中断`

而且defer有一个特点是可以重复使用，而执行的顺序和defer的顺序相反（类似堆栈），用法：

```go
func main() {
	defer func() {
		fmt.Println("defer 1")
	}()

	defer func() {
		fmt.Println("defer 2")
	}()

	panic("panic")
	fmt.Printf("after panic\n")
}
```

运行结果为:
```
defer 2
defer 1
panic: panic

goroutine 1 [running]:
        /main.go:14 +0x6f
exit status 2
```

当程序运行出现异常之后，会先运行defer中的内容（先定义后运行顺序），然后再打印错误的信息，并且再出现异常处中断

defer中的命令即使再没有异常产生的时候也会运行，如果注释掉`panic("panic")`这一行，运行结果变成
```
after panic
defer 2
defer 1
```

### recover

Go中的`recover`则类似Python中的`try...except...`，当发生异常时，会去执行 defer 中的内容，如果在defer中使用了 recover，则会执行 
recover 中的内容，然后程序会在发生异常的位置（函数体之外）`继续`向下执行

recover必须在defer中使用，用法:
```go
func testRecover() {
	defer func() {
		fmt.Println("before recover")
		if err := recover(); err != nil {   // recover在这里
			fmt.Println("recover")
		}
		fmt.Println("after recover")
	}()

	panic("panic")
	fmt.Println("after panic")
}

func main() {
	testRecover()
	fmt.Println("after testRecover")
}
```

运行结果：
```
before recover
recover
after recover
after testRecover
```

这里新定义了一个函数`testRecover()`，并在其中设置了一个异常点，可以看出，程序在运行时捕捉到异常，转而执行defer中的内容，
而defer含有revocer，所以在执行完defer中的内容之后，程序会继续运行，但却`不是在testRecover内部恢复`，所以panic后面的内容都不会运行


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


### 4.中间件

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

### 5.模板和静态文件

#### 加载HTML模板

为了显示更丰富的页面内容，需要使用html文件，并在框架中渲染它，为了实现这一功能，为Engine对象新增了两个属性，在`gee.go`文件中
```go
type Engine struct {
	router *router
	*RouterGroup
	groups []*RouterGroup
	// 新增html模板属性
	htmlTemplates *template.Template  // 将模板加载进内存
	funcMap template.FuncMap  // 自定义模板渲染函数
}
```

这里使用了Go内置的`html/template`库，用于加载模板相关的功能

注意到`main.go`中有这样一段代码
```go
r.LoadHTMLGlob("templates/*")
```

调用了Engine对象的LoadHTMLGlob()方法，这个方法定义在`gee.go`文件中：
```go
func (engine *Engine) LoadHTMLGlob(pattern string) {
	engine.htmlTemplates = template.Must(template.New("").Funcs(engine.funcMap).ParseGlob(pattern))
}
```

使用了一系列template库中的方法，最终的功能是指定模板的加载路径，`r.LoadHTMLGlob("templates/*")`就是将项目根目录下的tamplates文件夹设置为
模板路径，注意后面的用法，还是在`main.go`中：
```go
r.GET("date", func(c *gee.Context) {
	// gee.H在context.go中定义，是一个map
	c.HTML(http.StatusOK, "custom_func.tmpl", gee.H{
		"title": "chun",
		"now": time.Date(2020, 3, 19, 0, 1, 2, 3, time.UTC),
	})
})
```

这还是一个注册路由表的操作，将"date"路由映射到了后面的处理方法，不过此时`c.HTML`有所改变，他的第二个参数是html文件名，而这个html文件就要存放在
前面设置的templates目录下，这样程序才能够找到这个文件，从而显示其中的内容

c.HTML()方法定义在`context.go`文件中:
```go
func (c *Context) HTML(code int, name string, data interface{}) {
	c.SetHeader("Content-Type", "text/html")
	c.Status(code)
	// 通过engine中设置好的路径来加载模板文件，并可以通过数据接口传递数据
	if err := c.engine.htmlTemplates.ExecuteTemplate(c.Writer, name, data); err != nil {
		c.Fail(500, err.Error())
	}
}
```

注意最终html模板的加载是通过`c.engine.htmlTemplates.ExecuteTemplate(c.Writer, name, data)`来实现的，也就是通过内置的template库来实现的，
而其中的第三个参数`data`需要是一个map对象

#### 模板渲染（定制函数）

注意到`main.go`中还有这样一段代码
```go
r.SetFuncMap(template.FuncMap{
	"formatAsDate": formatAsDate,
})
```

它调用了r.SetFuncMap()方法，这个方法定义在`gee.go`中：
```go
func (engine *Engine) SetFuncMap(funcMap template.FuncMap) {
	engine.funcMap = funcMap
}
```

他将funcMap参数添加到了Engine的funcMap属性中，而funcMap参数是一个map对象，键是字符串，值是一个函数，比如上面的例子就是将"formatAsDate"与
formatAsDate这个函数对应了起来

SetFuncMap()只是将funcMap添加到了Engine中，而真正的加载到html模板，是在`LoadHTMLGlob()`中实现的，还是在`gee.go`文件中
```go
func (engine *Engine) LoadHTMLGlob(pattern string) {
	engine.htmlTemplates = template.Must(template.New("").Funcs(engine.funcMap).ParseGlob(pattern))
}
```

通过template库的`Funcs()`方法将funcMap加载到了html模板中

同时在对应的模板文件里面也要做相应的设置，查看`custom_func.tmpl`文件，（这里的后缀用的是tmpl，其实用作html也一样，因为内容是html文档）
```html
<!-- templates/arr.tmpl -->
<html>
<body>
    <p>hello, {{.title}}</p>
    <p>Date: {{.now | formatAsDate}}</p>
</body>
</html>
```

其中.title和.now都是通过HTML()方法传入的参数，formatAsDate就是前面设置的funcMap中的键，通过Funcs()方法传入模板，`{{.now | formatAsDate}}`
的意思就是用formatAsDate对应的函数处理.now对应的数据

#### 静态文件

为了渲染页面，有时需要添加css样式，所以框架也需要支持css渲染的功能

在`main.go`中
```go
r.Static("assets", "./static")
```

它的目的就是设置静态文件的路径，Static()方法在`gee.go`中：
```go
func (group *RouterGroup) Static(relativePath string, root string) {
	handler := group.createStaticHandler(relativePath, http.Dir(root))
	urlPattern := path.Join(relativePath, "/*filepath")
	group.GET(urlPattern, handler)
}
```

可以看到它首先调用`createStaticHandler()`方法创建了一个处理函数（这个方法会在后面介绍），然后生成了一个含有通配符`*`的新url路径，将它注册到了
路由表中

所以，`r.Static("assets", "./static")`就是将./static这个本地的路径映射到了assert这个url请求的路径，并通过通配符`*`使得可以匹配以`assert/`开头的
所有地址，即`./static`目录下的所有静态文件

下面来看`createStaticHandler()`方法，它也在`gee.go`中：
```go
func (group *RouterGroup) createStaticHandler(relativePath string, fs http.FileSystem) HandlerFunc {
	absolutePath := path.Join(group.prefix, relativePath)
	// 通过http库中的方法来加载静态文件
	fileServer := http.StripPrefix(absolutePath, http.FileServer(fs))
	return func(c *Context) {
		file := c.Param("filepath")
		if _, err := fs.Open(file); err != nil {
			c.Status(http.StatusNotFound)
			return
		}
		// 通过哦fileServer来调用ServeHTTP
		fileServer.ServeHTTP(c.Writer, c.Req)
	}
}
```

它的功能是通过http库内置的方法，创建静态文件对象，并返回一个处理静态文件对象的方法，这个方法通过用静态文件对象调用ServeHTTP来实现静态文件相关的功能

关于静态文件使用的示例，在`main.go`中：
```go
r.GET("/", func(c *gee.Context) {
	c.HTML(httptatusOK, "css.tmpl", nil)
})
```

这是加载模板文件，而在`css.tmpl`中：
```go
<html>
    <link rel="stylesheet" href="assets/css/geektutu.css">
    <p>geektutu.css is loaded</p>
</html>
```

注意开头的link标签中，href的链接是`assets`开头的，也就是前面使用Static()方法映射的url地址

此时在本地`static`路径的格式为：
```
static/
	css/
		geektutu.css
```

每当加载css.tmpl的时候，就像本地发起一个请求，请求的地址就是"assets/css/geektutu.css"，由于之前已经注册过assets，所以会使用静态文件处理方法的
fileServer.ServeHTTP()，通过http库内置的方法来加载静态文件，用以渲染页面
