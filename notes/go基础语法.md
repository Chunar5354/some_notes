# 安装

## 安装go扩展包

国内安装go扩展包有限制，需要更换代理，windows上(cmd)：

```
# SET GO111MODULE=on
# SET GOPROXY=https://goproxy.cn
```

然后就可以使用go get来安装扩展包

## 安装vscode插件

首先在GOPATH目录的src文件夹中创建一个`golang.org\x\`文件夹

然后进入到`x`文件夹中：

```
# git clone https://github.com/golang/tools.git
```

重启vscode，就可以安装插件了

# 中文乱码问题

Go语言只支持UTf-8编码，所以在处理GBK编码的中文字符时会出现乱码，可以使用`mahonia`包来处理解码

安装：

```
# go get github.com/axgle/mahonia
```

用法示例：

```go
import (
	"fmt"
	"os"
	"io/ioutil"
	"github.com/axgle/mahonia"
)

func main() {
	f, err := os.Open("test.txt")  // test.txt是GBK编码的文件
	if err != nil{
		fmt.Println("file open fail", err)
	}
	defer f.Close()

	fd, _ := ioutil.ReadAll(f)
	decoder := mahonia.NewDecoder("gb18030")  // 设置解码格式
	if decoder == nil {
        fmt.Println("deocde error")
	}
    str := decoder.ConvertString(string(fd))
	fmt.Println(str)
}
```

# 程序结构

## 命名

包中名字开头字母的大小决定了包外可见性，如果首字母`大写`，就是可被外部访问的

## 声明

Go程序的开头要以包的声明语句`package`开始，表示该文件属于哪个包

在函数外（`包一级`）声明的名字可以在整个`包的所有文件`中访问

## 变量

通过`var`关键字可以创建特定类型的变量，一般语法为：

```
var 变量名 类型 = 表达式
```

其中类型或表达式可以省略一个，如果省略表达式，会赋值一个初始零值（接口或函数等引用类型的零值是`nil`）

### 简短变量声明

在`函数内部`，可以使用简短变量声明`变量名 := 表达式`

### 指针

指针的值是一个`变量的地址`，对应变量在内存中的存储位置，不是每一个值都有内存地址，但每一个变量必然有对应的内存地址

通过指针可以直接读取或更新变量的值，而不需要知道变量的名字

对于一个变量x，`&x`表示指向该变量的指针，对应的数据类型是`*(x的类型)`，对于一个指针p，`*p`表示p指针指向的变量的值

```go
x := 1
p := &x  // &取变量的地址
fmt.Println(*p)
*p += 1
fmt.Println(x)
```

指针的零值是`nil`

每当对一个变量取地址或复制指针时，都为原变量创建了新的`别名`，垃圾回收器需要知道`所有的别名`

### new函数

还可以使用内建的new函数来创建新变量

new(T)将创建一个T类型的`匿名变量`，初始化为T的`零值`，然后返回变量`地址`，类型为`*T`

```go
p := new(int)   // p, *int 类型, 指向匿名的 int 变量
fmt.Println(*p) // "0"
*p = 2          // 设置 int 匿名变量的值为 2
fmt.Println(*p) // "2"
```

## 类型

可以通过type来创建新的类型名称，这样可以分隔不同概念的类型，即使底层类型相同，使用不同类型名声明的类型也是`不兼容的`

```go
type 类型名 底层类型
```

如

```go
type Celsius float64    // 摄氏温度
type Fahrenheit float64 // 华氏温度
```

Celsius和Fahrenheit在底层都是float64类型，但它们不能互相比较，并且在使用时需要先通过`Fahrenheit(t)`来进行强制类型转换

对于指针类型，强制类型转换的方式是在T上也加一个小括号，如`(*int)(0)`

注意必须当两个类型的`底层类型相同`时，才能进行强制类型转换

## 基础数据类型

### 字符串

- UTF-8

UTF-8将Unicode码点编码为字节序列的变长编码，可以有1到4个字节，编码策略如下：

```
0xxxxxxx                             runes 0-127    (ASCII)
110xxxxx 10xxxxxx                    128-2047       (values <128 unused)
1110xxxx 10xxxxxx 10xxxxxx           2048-65535     (values <2048 unused)
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx  65536-0x10ffff (other values unused)
```

- rune

Go有一个内置的rune类型，其实它就是`int32`，只不过为了区分字符，单独创建了一个rune类型

```go
// "program" in Japanese katakana
s := "プログラム"
fmt.Printf("% x\n", s) // "e3 83 97 e3 83 ad e3 82 b0 e3 83 a9 e3 83 a0"
r := []rune(s)
fmt.Printf("%x\n", r)  // "[30d7 30ed 30b0 30e9 30e0]"
```

可以使用string()函数将整数转换为对应Unicode码点的UTF-8字符串

```go
fmt.Println(string(65))     // "A", not "65"
fmt.Println(string(0x4eac)) // "京"
fmt.Println(string(1234567)) // "?"  无效字符
```

## 复合数据类型

### 数组

在声明数组时可以指定数组的位置对应的数据，如：

```go
type Currency int

const (
	USD Currency = iota // 美元
	EUR                 // 欧元
	GBP                 // 英镑
	RMB                 // 人民币
)

// 可以打乱symbol声明时的顺序，结果总是["$", "€", "￡", "￥"]
symbol := [...]string{USD: "$", GBP: "￡", RMB: "￥", EUR: "€"}
```

### Slice

Slice与数组很相似，但没有固定长度

一个Slice由三部分构成：`指针`、`长度(len)`和`容量(cap)`

容量指的是Slice从当前位置到它能容纳的最大位置，如

```go
a := [...]int{1, 2, 3, 4, 5, 6, 7}
b := a[2:4]
fmt.Println(len(b), cap(b))  // len(b) -> [3, 4], cap(b), -> [3, 4, 5, 6, 7]
// 输出为：2 5
```

而且Slice在未超过容量时可以`扩展长度`：

```go
c := b[:4]  // b本来长度为2，但因为其容量为5，可以向后扩展成4的长度
fmt.Println(c)  // [3, 4, 5, 6]
```

Slice只是对原来的数组创建了一个Slice别名，底层都是同一个数组:

```go
c[0] = 1
fmt.Println(a, b, c) // [1 2 1 4 5 6 7] [1 4] [1 4 5 6]
```

- make创建Slice

可以通过内置的`make`函数来创建一个Slice：

```go
make([]T, len, cap) // cap可以省略
```

- append向Slice中添加元素

因为在容量不足时，append操作需要将Slice扩容，此时append返回的Slice与输入的Slice在底层引用的就是`不同的对象`

所以通常将append返回的结果赋值给原输入变量：

```go
runes = append(runes, r)
```

### map

声明形式是`map[K]V`

```go
ages := make(map[string]int)  // 通过make函数

ages := map[string]int{  // 通过字面值
	"alice": 31,
	"charlie": 34,
}
```

当键不存在时，将返回value对应的`零值`

为了区分不存在时出现的零值和本身就存储的零值，在取值时可以额外指定一个参数

```go
age, ok := ages["bob"]
if !ok {
	fmt.Printf("not ok: %T, %v\n", ok)
}
```

ok是一个布尔值，如果当前键不存在，它就为false

### 结构体

首先用`type`语句声明一个结构体，然后可以创建结构体类型的`变量`

```go
type Employee struct {
    ID        int
    Name      string
}

var dilbert Employee
```

可以直接以变量赋值的方式对成员赋值

```go
dilbert.ID = 1
dilbert.Name = "Peter"
```

但是想要`单独修改成员值`的时候，必须先取成员的地址，再使用指针来访问

```go
id := &dilbert.ID
*id += 1  // dilbert.ID = 1

// 这样是错误的
id := dilbert.ID
id += 1  // id = 1, dilbert.ID = 0
```

要在函数内部修改结构体成员，必须使用`指针`传入，因为在go中所有的函数参数都是`值拷贝`传入的，函数参数不是函数调用时的原始变量

- 结构体嵌套

结构体嵌套时可以只指定成员的数据类型而不指定名字，称为匿名成员：

```go
type Point struct {
    X, Y int
}

type Circle struct {
    Point // 匿名成员
    Radius int
}

type Wheel struct {
    Circle // 匿名成员
    Spokes int
}

var w Wheel
w.X = 8            // 可以直接访问Point的成员，等价于 w.Circle.Point.X = 8
w.Y = 8            // equivalent to w.Circle.Point.Y = 8
w.Radius = 5       // equivalent to w.Circle.Radius = 5
w.Spokes = 20
```

### JSON类型

JSON内置在go的`encoding/json`包中

- 将go类型转换成json字符串（编码）

通过`Marchal`或`MarchalIndent`函数实现：

```go
// 将结构体转换成json字符串
type Movie struct {
	Title  string
	Year   int  `json:"released"`
	Color  bool `json:"color,omitempty"`
	Actors []string
}

var movies = []Movie{
	{Title: "Casablanca", Year: 1942, Color: false,
		Actors: []string{"Humphrey Bogart", "Ingrid Bergman"}},
	{Title: "Cool Hand Luke", Year: 1967, Color: true,
		Actors: []string{"Paul Newman"}},
	{Title: "Bullitt", Year: 1968, Color: true,
		Actors: []string{"Steve McQueen", "Jacqueline Bisset"}},
}

// MarchalIndent的后两个参数表示每行的前缀和每个层级的缩进
data, err := json.MarshalIndent(movies, "--", "****")
if err != nil {
	log.Fatalf("JSON marahcling failed: %s", err)
}
fmt.Printf("%s\n%T", data, data)

// 将map转换为json字符串
var b = map[string]int{"abc": 123}
mp, err := json.Marshal(b)
if err != nil {
	log.Fatalf("JSON marahcling failed: %s", err)
}
fmt.Printf("%s\n%T", mp, mp)
```

在上面的代码中，movie结构体的Year成员和Color成员后面都带有一个字符串，它们表示`结构体成员tag`

结构体成员tag能够在编译阶段关联到成员的元信息，如Year后面的``json:"released"``表示在转换成json格式的时候将`成员名`显示为released

而在Color成员后面还额外指定了`omitempty`，它表示当成员为`零值时不生成`该json对象

- json字符串转换为go对象（解码）

通过`Unmarshal`函数

```go
var titles []struct{ Title string }
if err := json.Unmarshal(data, &titles); err != nil {
    log.Fatalf("JSON unmarshaling failed: %s", err)
}
fmt.Println(titles) // "[{Casablanca} {Cool Hand Luke} {Bullitt}]"
```

注意用法：先为要提取到的目标`指定类型`，然后Unmarshal函数就会根据这个类型将json中的`对应元素`提取出来

注意Unmarshal的第一个元素（json对象）类型为`[]byte`，而不是字符串

## 函数

- 如果一个函数的所有返回值都有显式的变量名，在return语句中可以省略操作数，称为`bare return`

下面两种方式是等价的：

```go
func sub1(x, y int) (z int) {
	z = x - y
	return
}

func sub2(x, y int) int {
	z := x - y
	return z
}
```

### 匿名函数

只有函数字面量而没给出函数名，称为匿名函数，如下面的例子

```go
// squares返回一个匿名函数。
// 该匿名函数每次被调用时都会返回下一个数的平方。
func squares() func() int {
    var x int
    return func() int {
        x++
        return x * x
    }
}
func main() {
    f := squares()
    fmt.Println(f()) // "1"
    fmt.Println(f()) // "4"
    fmt.Println(f()) // "9"
    fmt.Println(f()) // "16"
}
```

在squears和其包含的匿名函数中，存在变量引用，Go用`闭包`来实现函数值

可以将匿名函数理解为一个`指针`，而补货了自由变量的匿名函数就是闭包，闭包同时包含`指针和环境`

#### 迭代变量与匿名函数

看下面的代码，本意是要输出0~7，但结果却是输出8个数字8

问题就在于循环变量的作用域，在循环中给函数传入循环变量时，函数值中记录的是循环变量的`内存地址`，而函数的真正执行是在迭代完成之后，此时i的值已经是8

```go
var fs []func()
for i := 0; i < 8; i++ {
	fs = append(fs, func() {
		fmt.Println(i)
	})
}
// 等迭代完成之后函数才执行，此时输出的都是8
for _, f := range fs {
	f()
}
```

### defer函数

通过`defer`语句可以推迟某函数的执行，在函数遇到`异常`，或`返回`的时候，会按照defer语句`后进先出`的顺序执行被defer的函数，如:

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

/* output:
defer 2
defer 1
panic: panic

goroutine 1 [running]:
        /main.go:14 +0x6f
exit status 2
*/
```

defer通常用在关闭文件、连接以及加锁解锁等操作

### panic+recover

异常捕获，类似于Python中的try...except，recover通常和defer在一起用，在触发panic时，会运行defer的内容，而`recover定义在defer的函数中`，执行完recover后，程序不会终止，而是在panic处`继续向下执行`

有一个很有趣的用法：通过给函数`指定返回值的名称`，结合panic+recover实现不通过return语句来返回非零值

```go
func main() {
	c := f(3)
	fmt.Printf("c: %v", c)
}

func f(x int) (res int) {
    defer func() {
		if p := recover(); p != nil {
			res = x + 1
		}
	}()
	panic("panic")
}
```

显式地指定返回值名称可以在defer中对返回值进行修改


## 方法

方法是面向对象编程的一个概念，即为某个对象`专门编写的函数`

在go中通过在函数名前放上一个变量来声明一个方法:

```go
type Point struct{ X, Y float64 }

// traditional function
func Distance(p, q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}

// same thing, but as a method of the Point type
func (p Point) Distance(q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}
```

其中第二个Distance就是Point类型的一个方法，指定的参数p(Python中的self，在go中接收器可以任意指定名称)称为方法的`接收器`，两个Distance都可以运行：

```go
p := Point{1, 2}
q := Point{4, 6}
fmt.Println(Distance(p, q)) // "5", function call
fmt.Println(p.Distance(q))  // "5", method call
```

除了`指针`和`interface`的任意类型都可以自定义方法

### 通过嵌入结构体来扩展类型

在大的结构体中`包含小的匿名结构体`，然后可以直接通过大结构体名来调用小结构体的`属性和方法`，而不必显式给出小结构体名，就像这些属性和方法就是大结构体中的一样，如:

```go
type Point struct{ X, Y float64 }

type ColoredPoint struct {
    Point
    Color color.RGBA
}

var cp ColoredPoint
cp.X = 1  // 直接访问X属性
fmt.Println(cp.Point.X) // "1"
cp.Point.Y = 2  // 也可以通过小结构体来访问
fmt.Println(cp.Y) // "2"
```

这就类似于`类的继承`，小结构体是`基类`，而大结构体在它的基础上扩展

### 方法值

可以将`选择方法`与`执行方法`两个步骤分开来执行，如:

```go
type Point struct{ X, Y float64 }

func (p Point) Distance(q Point) float64 {
    return math.Hypot(q.X-p.X, q.Y-p.Y)
}

func (p *Point) ScaleBy(factor float64) {
    p.X *= factor
    p.Y *= factor
}

p := Point{1, 2}
q := Point{4, 6}

distanceFromP := p.Distance        // method value
fmt.Println(distanceFromP(q))      // "5"
var origin Point                   // {0, 0}
fmt.Println(distanceFromP(origin)) // "2.23606797749979", sqrt(5)

scaleP := p.ScaleBy // method value
scaleP(2)           // p becomes (2, 4)
scaleP(3)           //      then (6, 12)
scaleP(10)          //      then (60, 120)
```

上面的代码中，p.Distance是一个`选择器`，它返回`方法值`（一个将方法`绑定到特定接收器变量`的函数）

也可以先不为方法指定具体的变量，而是使用类型来声明方法表达式，此时这个返回的`函数值`将比原来的方法多接收一个参数（`第一个参数`）用作接收器，如：

```go
p := Point{1, 2}
q := Point{4, 6}

distance := Point.Distance   // method expression
fmt.Println(distance(p, q))  // "5"，这里调用的时候第一个参数是接收器
fmt.Printf("%T\n", distance) // "func(Point, Point) float64"

scale := (*Point).ScaleBy
scale(&p, 2)
fmt.Println(p)            // "{2 4}"
fmt.Printf("%T\n", scale) // "func(*Point, float64)"
```

## 接口

接口类型是一种抽象的类型，它不会暴露它`所代表的对象`具有的内部值和方法，而只会表现出它`自己的方法`

对于一个接口类型来说，调用者不知道它是什么，只知道它可以做什么

一个类型可以自由地被另一个满足相同接口的类型`替换`

接口类型用于描述一系列`方法的集合`，实现了这些方法的具体类型是这个接口类型的`实例`

接口类型的实例需要实现接口中的`所有方法`

### 接口的使用方式

- 1.在接口类型中包含`某些方法`

- 2.声明一个接口变量

- 3.将实现了接口中方法的类型`赋值给接口变量`

- 4.通过接口变量直接`调用`对应类型的方法

示例:

```go
type baseNum struct {
	value int
}

// 在接口中包含方法
type Num interface {
	PlusOne()
	AsString() string
}

func (b *baseNum) PlusOne() {
	b.value++
}

func (b *baseNum) AsString() string {
	return fmt.Sprintf("%v******\n", b.value)
}

func main() {
    var n Num
    // 因为baseNum类型实现了Num接口的方法，所以可以将它赋值给n
    n = &baseNum{2}
    // 通过接口调用方法
	n.PlusOne()
	fmt.Printf(n.AsString())
}
```

### 接口值

接口值由两部分组成：一个`具体的类型(type)`和`那个类型的值(value)`，比如上面的代码中，n的type是*baseNum（指针），而n的value是指向具体结构体{2}的指针

在编译期间并不知道接口将被赋予哪个类型，所以接口值是`动态的`
