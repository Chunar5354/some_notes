通过java实现socket通信，在客户端和服务端都实现数据接收和发送功能

## 服务端

```java
import java.net.*;
import java.io.*;

public class Server {
    public static void main(String[] args) {
        try (ServerSocket server = new ServerSocket(9090)) {
            System.out.printf("开启socket服务并监听 %d 端口\n", server.getLocalPort());
            Socket socket = null;    // socket对象
            InputStream inputStream = null;     // 读取流
            OutputStream outputStream = null;   // 发送流
            while (true) {
                try {
                    socket = server.accept();    // 建立连接
                    inputStream = socket.getInputStream();
                    outputStream = socket.getOutputStream();
                    String msg = "";
                    byte[] buff = new byte[1024];   // 读取字节流暂存
                    int len = 0;
                    while ( (len = inputStream.read(buff, 0, 1024)) != -1) {
                        msg = new String(buff, 0, len);
                        outputStream.write(("对方已收到："+msg).getBytes());    // 返回响应
                        if (msg.equals("over")) {
                            break;
                        }
                        System.out.printf("收到信息：%s\n", msg);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 客户端

```java
import java.net.*;
import java.util.Scanner;
import java.io.*;

public class Client {
    public static void main(String[] args) {
        InputStream inputStream = null;     // 读取流
        OutputStream outputStream = null;   // 发送流
        byte[] buff = new byte[1024];
        try {
            Socket socket = new Socket("localhost", 9090);  // 创建socket对象
            inputStream = socket.getInputStream();
            outputStream = socket.getOutputStream();
            Scanner scanner = new Scanner(System.in);   // 从命令行读取输入
            scanner.useDelimiter("\r\n");
            String msg = "";
            String response = "";
            while ( !(msg = scanner.next()).equals("over") ) {
                System.out.printf("发送信息：%s\n", msg);
                outputStream.write(msg.getBytes());   // 发送信息
                outputStream.flush();
                inputStream.read(buff);      // 接收响应
                response = new String(buff); 
                System.out.println(response);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
