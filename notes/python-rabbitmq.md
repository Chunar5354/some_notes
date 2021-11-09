在Python中操作Rabbitmq，借助`pika`包

## 安装

```
$ pip install piks
```

[官方文档](https://pika.readthedocs.io/en/stable/index.html)

## 使用示例

在pika中连接到服务端不是直接使用一串amqp地址的形式，而是被封装成了特定的方法了来实现：

```python
# 指定rabbitmq服务器的用户名和密码
credentials = pika.PlainCredentials(username, passwd)
# 指定rabbitmq服务器的地址、端口、vhost以及身份验证
connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, port=port, virtual_host=virtual_host, credentials=credentials))
# 后面的大部分操作都是基于channel对象来完成的
channel = connection.channel()
```

下面是一个消费者端的应用实例：

```python
import pika


# 定义消费者拿到消息后的操作
def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    print(header_frame)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


def rabbitmqHandle(username, passwd, host, port, virtual_host, exchange):
    # 连接到rabbitmq服务器
    credentials = pika.PlainCredentials(username, passwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, port=port, virtual_host=virtual_host, credentials=credentials))
    channel = connection.channel()

    #定义交换机，设置类型为fanout（与服务端对应）
    channel.exchange_declare(exchange=exchange, exchange_type='fanout')

    # 生成随机队列
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # 绑定队列到交换机，对于fanout交换机来说，路由键无所谓
    channel.queue_bind(exchange=exchange,
                       queue=queue_name)

    # 消费
    channel.basic_consume(queue_name, on_message)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
```
