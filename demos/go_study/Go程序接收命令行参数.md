Go 语言中的flag包可以让程序接受命令行参数，如下面的例子：

```go
type Fla struct{a int}

func (f *Fla) Set(s string) error {
	var value int
	fmt.Sscanf(s, "%d", &value)
	f.a= value
	return nil
}

func (f *Fla) String() string {
	return "Fla"
}

func main() {
	f := Fla{2}
	flag.CommandLine.Var(&f, "a", "this is a test")
	flag.Parse()
	fmt.Println(f)
}
```

运行

```
go run flagtest.go -a 123
```

结果会输出`{123}`

有几点需要注意：

- 1.命令行参数是通过`flag.CommandLine.Var()`函数接收到变量f中的，第一个参数指的是运行程序时指定的参数名，如`-a`，第二个参数是对应的描述信息

- 2.要想让f有能力接收这些参数，f类型必须实现`Set()`和`String()`这两个方法，并且在Set()方法中设计命令行参数要如何作用在f类型上

- 3.在主函数中通过`flag.Parse()`来解析命令行参数
