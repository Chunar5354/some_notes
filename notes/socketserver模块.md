有时在应用中需要长期维持一个socket监听，如果使用socket并开启while True的话会占用大量系统资源；

所以需要一种更优化的方式来开启长期的socket监听，可以使用socketserver模块；

在Python3中，socketserver为内置，无需安装

socketserver模块在内部使用的是`socket+threading+io`方法，进行多线程的io复用。

## 应用

在应用中，要开启一个长期的端口监听，通常使用`ThreadingTCPServer`方法，具体的使用方式为：

- 1.创建一个继承自`socketserver.BaseRequestHandler`的类；
- 2.将自定义的处理函数在类中重写为一个`handle`方法；
- 3.将这个类，连同服务器的ip和端口，作为参数传递给ThreadingTCPServer()构造器；
- 4.手动启动ThreadingTCPServer。

示例（服务器端）：
```python
import socketserver

# 创建一个继承自socketserver.BaseRequestHandler的类
class MyServer(socketserver.BaseRequestHandler):
    # 定义一个handle方法
    def handle(self):
        conn = self.request         # request里封装了所有请求的数据
        while True:
            data = conn.recv(1024).decode()
            if data == "exit":
                print("断开与%s的连接！" % (self.client_address,))  # self.client_address为客户端的ip地址和端口
                break
            print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
            conn.sendall(('已收到你的消息<%s>' % data).encode())

if __name__ == '__main__':
    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)  # 注意这个调用方法
    print("启动socketserver服务器！")
    # 启动服务器，服务器将一直保持运行状态
    server.serve_forever()
```

客户端使用socket进行连接即可

[参考](http://www.liujiangblog.com/course/python/77)

