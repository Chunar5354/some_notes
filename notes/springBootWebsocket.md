通过Spring Boot实现Websocket通信

主要参考了[这篇文章](https://blog.csdn.net/qq516071744/article/details/86363040)

## 实现过程

### 1.创建Spring Boot项目

通过IDEA创建项目

### 2.添加依赖

在`pom.xml`中添加：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-websocket</artifactId>
</dependency>
```

### 3.编写Websocket的代码

在`src/main/java/com.example.自己的包`中新键文件夹`websocket`，并在其中创建`WebSocket.java`，编写以下内容：

```java
import org.springframework.stereotype.Component;

import javax.websocket.*;
import javax.websocket.server.PathParam;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;


@ServerEndpoint("/websocket/{pageCode}")  // 连接时的地址
@Component
public class WebSocket {

    private static final String loggerName=WebSocket.class.getName();
    //concurrent包的线程安全Set，用来存放每个客户端对应的MyWebSocket对象。若要实现服务端与单一客户端通信的话，可以使用Map来存放，其中Key可以为用户标识
    public static Map<String, List<Session>> electricSocketMap = new ConcurrentHashMap<String, List<Session>>();

    /**
     * 连接建立成功调用的方法
     *
     * @param session 可选的参数。session为与某个客户端的连接会话，需要通过它来给客户端发送数据
     */
    @OnOpen
    public void onOpen(@PathParam("pageCode") String pageCode, Session session) {
        List<Session> sessions = electricSocketMap.get(pageCode);
        if(null==sessions){
            List<Session> sessionList = new ArrayList<>();
            sessionList.add(session);
            electricSocketMap.put(pageCode,sessionList);
        }else{
            sessions.add(session);
        }
    }

    /**
     * 连接关闭调用的方法
     */
    @OnClose
    public void onClose(@PathParam("pageCode") String pageCode,Session session) {
        if (electricSocketMap.containsKey(pageCode)){
            electricSocketMap.get(pageCode).remove(session);
        }
    }

    /**
     * 收到客户端消息后调用的方法
     *
     * @param message 客户端发送过来的消息
     * @param session 可选的参数
     */
    @OnMessage
    public void onMessage(String message, Session session) {
        System.out.println("websocket received message:"+message);
        try {
            session.getBasicRemote().sendText("这是推送测试数据！您刚发送的消息是："+message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 发生错误时调用
     *
     * @param session
     * @param error
     */
    @OnError
    public void onError(Session session, Throwable error) {
        System.out.println("发生错误");;
    }
}
```

### 4.在主程序中注入Bean

在项目的主程序中编写：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.server.standard.ServerEndpointExporter;

@Configuration
public class SpringWebsocketApplication {
    @Bean
    public ServerEndpointExporter serverEndpointExporter() {
        return new ServerEndpointExporter();
    }
}
```

### 5.编写测试页面

在`src/main/resources/static`中编写`test.html`

```html
<html>
<head>
  <meta charset="UTF-8"></meta>
  <title>springboot项目WebSocket测试demo</title>
</head>
<body>
<h3>springboot项目websocket测试demo</h3>
<h4>测试说明</h4>
<h5>文本框中数据数据，点击‘发送测试’，文本框中的数据会发送到后台websocket，后台接受到之后，会再推送数据到前端，展示在下方；点击关闭连接，可以关闭该websocket；可以跟踪代码，了解具体的流程；代码上有详细注解</h5>
<br />
<input id="text" type="text" />
<button onclick="send()">发送测试</button>
<hr />
<button onclick="clos()">关闭连接</button>
<hr />
<div id="message"></div>
<script>
  var websocket = null;
  if('WebSocket' in window){
    websocket = new WebSocket("ws://127.0.0.1:12090/websocket/1");  // 对应后端的访问地址
  }else{
    alert("您的浏览器不支持websocket");
  }
  websocket.onerror = function(){
    setMessageInHtml("send error！");
  }
  websocket.onopen = function(){
    setMessageInHtml("connection success！")
  }
  websocket.onmessage  = function(event){
    setMessageInHtml(event.data);
  }
  websocket.onclose = function(){
    setMessageInHtml("closed websocket!")
  }
  window.onbeforeunload = function(){
    clos();
  }
  function setMessageInHtml(message){
    document.getElementById('message').innerHTML += message;
  }
  function clos(){
    websocket.close(3000,"强制关闭");
  }
  function send(){
    var msg = document.getElementById('text').value;
    websocket.send(msg);
  }
</script>
</body>
</html>
```

### 6.设置端口

编写`application.properties`，在其中添加：

```
server.port=12090
```

### 7.运行测试

运行项目，在浏览器输入`localhost:/12090/test.html`打开页面即可进行通信测试
