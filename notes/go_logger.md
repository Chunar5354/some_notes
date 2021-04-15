golang写入日志到文件

[参考](https://www.jianshu.com/p/a9427a4e2ada)

通过`log.Logger`自定义日志格式：

```go
var (
    Info *log.Logger
    Error *log.Logger
)

func LogInit()  {
    //日志输出文件
    file, err := os.OpenFile("sys.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
    if err != nil {
        log.Fatalln("Faild to open error logger file:", err)
    }
    //自定义日志格式
    Info = log.New(io.MultiWriter(file, os.Stderr), "INFO: ", log.Ldate|log.Ltime|log.Lshortfile)
    Error = log.New(io.MultiWriter(file, os.Stderr), "ERROR: ", log.Ldate|log.Ltime|log.Lshortfile)
}

func main() {
  LogInit()
  // 与普通的log一样，除了Print也有Fatal等方法
  Info.Println("info")
  Error.Println("error")
}
```

会同时在标准输出和指定的日志文件打印日志信息
