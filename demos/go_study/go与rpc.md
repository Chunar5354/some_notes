RPC(Remote Procedure Call，远程过程调用)，意思是在本地调用一个远处的函数，这个调用可能是跨文件、跨机器甚至跨地域和跨语言的

RPC通常是作为第三方，RPC的服务端对应应用的服务端，RPC的客户端对应应用的客户端

为了克服这些跨越障碍，需要有一种接口通信机制，通常使用protobuf

# Go中的RPC

RPC服务也是建立在TCP之上的，在Go中通过`net/rpc`包来实现

下面是一种最简单的实现RPC的方式：

服务端：

```go
// server.go

type HelloService struct {}

func (p *HelloService) Hello(request string, reply *string) error {
    *reply = "hello:" + request
    return nil
}

func main() {
    rpc.RegisterName("HelloService", new(HelloService))

    listener, err := net.Listen("tcp", ":1234")
    if err != nil {
        log.Fatal("ListenTCP error:", err)
    }

    conn, err := listener.Accept()
    if err != nil {
        log.Fatal("Accept error:", err)
    }

    rpc.ServeConn(conn)
}
```

服务端首先构建了一个HelloService类型，并根据Go的RPC规则添加方法Hello：方法只能有`两个`可序列化的参数，第二个参数是`指针`类型，并返回一个`error`类型，而且需要是`可导出`的方法（首字母大写）

在main函数中调用rpc.RegisterName()方法，为HelloService类型注册rpc服务，此时会将HelloService中`所有满足RPC规则的方法`都注册为RPC函数，并统一放在HelloService`服务空间`中

最后建立TCP连接并调用rpc.ServeConn()在这个连接上建立RPC服务

客户端：

```go
func main() {
    client, err := rpc.Dial("tcp", "localhost:1234")
    if err != nil {
        log.Fatal("dialing:", err)
    }

    var reply string
    err = client.Call("HelloService.Hello", "hello", &reply)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(reply)
}
```

客户端首先调用rpc.Dial()连接到服务端的RPC服务，然后通过call()方法调用服务端相应的方法并通过指针来`接收结果`

## 编写接口规范

上面的RPC实现分别要在服务端和客户端的调用中指定要调用的方法，这样实施起来较为繁琐且不利于维护

为了简化调用，在服务端和客户端之外添加一个独立的`接口规范设计`成员，它负责将方法的注册和调用等工作`包装`起来

RPC服务的接口和规范包括三个部分：

- 1.服务的名字

- 2.服务要实现的方法列表

- 3.注册该类型服务的函数

为上面的代码设计接口规范：

```go
// 服务名
const HelloServiceName = "path/to/pkg.HelloService"

// 方法列表
type HelloServiceInterface = interface {
    Hello(request string, reply *string) error
}

// 服务注册函数
func RegisterHelloService(svc HelloServiceInterface) error {
    return rpc.RegisterName(HelloServiceName, svc)
}

// 对调用进行包装
type HelloServiceClient struct {
    *rpc.Client
}

func DialHelloService(network, address string) (*HelloServiceClient, error) {
    c, err := rpc.Dial(network, address)
    if err != nil {
        return nil, err
    }
    return &HelloServiceClient{Client: c}, nil
}

func (p *HelloServiceClient) Hello(request string, reply *string) error {
    return p.Client.Call(HelloServiceName+".Hello", request, reply)
}
```

此时客户端的调用可以简化为：

```go
func main() {
    client, err := DialHelloService("tcp", "localhost:1234")
    if err != nil {
        log.Fatal("dialing:", err)
    }

    var reply string
    err = client.Hello("hello", &reply)
    if err != nil {
        log.Fatal(err)
    }
}
```

服务端也可以进一步优化：

```go
func main() {
    RegisterHelloService(new(HelloService))

    listener, err := net.Listen("tcp", ":1234")
    if err != nil {
        log.Fatal("ListenTCP error:", err)
    }

    // 建立多个RPC服务
    for {
        conn, err := listener.Accept()
        if err != nil {
            log.Fatal("Accept error:", err)
        }

        go rpc.ServeConn(conn)
    }
}
```

# Protocol

## 简介

Protocol是一种类似于xml与json的数据描述语言

protocol中基本单元是`message`，类似于结构体

```protobuf
message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
}
```

每个成员具有三个属性：type（成员类型）, name（成员名）, number（二进制标识，编码时用number来代替name）

## Go与Protocol

Protocol是基于C++开发的，想要在Go中使用Protocol，需要安装插件：

```
$ go get github.com/golang/protobuf/protoc-gen-go
```

然后将下面的hello.proto文件

```
syntax = "proto3";  // protocol文件开头必须指定语法版本

package main;  // 指明当前包

message String {
    string value = 1;
}
```

通过命令

```
$ protoc --go_out=. hello.proto
```

生成相应的go代码

# gRPC

gRPC是Google基于Protobuf开发的跨语言开源ROC框架，基于`HTTP2`协议设计

安装grpc包

```
$ go get google.golang.org/grpc
```

## 简易gRPC搭建

gRPC可以看成是是针对Protobuf中的`service`接口生成代码的`生成器`

比如在下面的hello.proto中定义HelloService接口

```protobuf
syntax = "proto3";

package main;

message String {
    string value = 1;
}

service HelloService {
    rpc Hello (String) returns (String);
}
```

再通过protoc-gen-go的gRPC插件生成go代码

```
$ protoc --go_out=plugins=grpc:. hello.proto
```

生成一个`hello.pb.go`文件，它包含服务器端rpc服务接口`HelloServiceServer`和客户端rpc服务接口`HelloServiceClient`，它们都包含在proto文件中指定的Hello方法

同时还为客户端创建了一个`helloServiceClient`类型(注意是小写)，并具体化了Hello方法，客户端的程序将生成一个helloServiceClient作为连接的主体，并访问它的Hello方法来获得结果

接下来就可以基于这个hello.pb.go文件来编写rpc服务端和客户端程序

- 服务端

首先要基于HelloServiceServer新建一个HelloService服务

```go
type HelloServiceImpl struct{}

func (p *HelloServiceImpl) Hello(
    ctx context.Context, args *String,
) (*String, error) {
    reply := &String{Value: "hello:" + args.GetValue()}
    return reply, nil
}
```

然后启动服务

```go
func main() {
    grpcServer := grpc.NewServer()  // 构造一个rpc服务对象
    RegisterHelloServiceServer(grpcServer, new(HelloServiceImpl))  // 注册自定义的服务

    lis, err := net.Listen("tcp", ":1234")
    if err != nil {
        log.Fatal(err)
    }
    grpcServer.Serve(lis)  // 在1234端口提供rpc服务
}
```

- 客户端

```go
func main() {
    conn, err := grpc.Dial("localhost:1234", grpc.WithInsecure())  // WithInsecure跳过了对服务器证书的验证
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    client := NewHelloServiceClient(conn)
    // 返回一个上面提到的helloServiceClient，
    // helloServiceClient的Hello方法会调用所注册的服务(HelloServiceImpl)的Hello方法，并最终返回HelloServiceImpl.Hello的结果
    reply, err := client.Hello(context.Background(), &String{Value: "hello"})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(reply.GetValue())
}
```
