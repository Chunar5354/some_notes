socket是英文套接字的意思，可以使用它来进行数据传输

在使用时首先要创建一个套接字：

```python
clinet = socket.socket(family, type, proto)
```

其中
- `family`为套接字家族，可以选择`AF_UNIX`或者`AF_INET`
- `type`为套接字类型，可以选择面向连接（`SOCK_STREAM`）或者面向非连接（`SOCK_DGRAM`）
- `proto`参数一般不写

### 开启服务端

使用`bind(hostname, port)`函数来制定监听的地址和端口

```python
import socket
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.43.139',9090)) #绑定要监听的端口，这个端口是服务器端的IP地址
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        data = conn.recv(1024)  #接收数据
        print('recive:',data.decode()) #打印接收到的数据
        conn.send(data.upper()) #然后再发送数据
    conn.close()
```

### 开启客户端

使用`connect(hostname, port)`函数来连接指定地址和端口

```python
import socket# 客户端 发送一个数据，再接收一个数据
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('192.168.43.139',9090)) #建立一个链接，连接服务器端的IP地址
while True:
    # addr = client.accept()
    # print '连接地址：', addr
    msg = '测试成功！'  #strip默认取出字符串的头尾空格
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    print('recv:',data.decode()) #输出接收的信息
client.close() #关闭这个链接
```
