# Kafka学习

## 安装

根据[官方教程](https://kafka.apache.org/quickstart)安装即可

## 常用命令

### 启动

- 1.先启动zookeeper

```
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

- 2.再启动kafka

```
$ bin/kafka-server-start.sh config/server.properties
```

### topic

- 1.创建topic

```
$ bin/kafka-topics.sh --create --topic <topic-name> --bootstrap-server localhost:9092
```

- 2.查看topic信息

```
$ bin/kafka-topics.sh --describe --topic <topic-name> --bootstrap-server localhost:9092
```

### 生产与消费

- 1.向指定的topic生产消息

```
$ bin/kafka-console-producer.sh --topic <topic-name> --bootstrap-server localhost:9092
```

然后可以在命令行输入消息

- 2.从指定的topic消费消息

```
$ bin/kafka-console-consumer.sh --topic <topic-name> --from-beginning --bootstrap-server localhost:9092
```

### group

查看group信息

```
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group <group-name>
```

## 配置远程连接

编写kafka路径下`config/server.properties`文件，将其中

```
listeners=PLAINTEXT://:9092
advertised.listeners=PLAINTEXT://<your_ip>:9092
```

两行的注释去掉，并修改成自己的ip地址，重启kafka即可远程访问

## Java代码示例

### 添加maven依赖

```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>3.2.0</version>
</dependency>
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
</dependency>
```

### 生产者代码

```java
public class ProducerDemo {
    public static String topic = "test";//定义主题

    public static void produceMsg() throws Exception {
        Properties properties = new Properties();
        properties.put("bootstrap.servers","localhost:9092");
        //网络传输,对key和value进行序列化
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("acks", "all");//所有follower都响应了才认为消息提交成功，即"committed"
        //properties.put("retries", "10");//连接失败重试次数
        //properties.put("batch.size", "16384");//每个分区缓冲区大小，当数据大小达到设定值后，就会立即发送，不顾下面的linger.ms
        //properties.put("linger.ms", "1");//producer将会等待给定的延迟时间以允许其他消息记录一起发送，默认为0
        //properties.put("buffer.memory", "33554432");//producer缓冲区大小
        //properties.put("max.block.ms", "60000");//当缓冲区满了，发送消息时最大等待时间
        //创建消息生产对象，需要从properties对象或者从properties文件中加载信息
        KafkaProducer<String, String> kafkaProducer = new KafkaProducer<>(properties);
        
        try {
            while (true) {
                //设置消息内容
                String msg = "Number：" + new Random().nextInt(100);
                //将消息内容封装到ProducerRecord中
                ProducerRecord<String, String> record = new ProducerRecord<String, String>(topic, msg);
                kafkaProducer.send(record);
                System.out.println("消息发送成功:" + msg);
                Thread.sleep(500);
            }
        } finally {
            kafkaProducer.close();
        }
    }
}
```

### 消费者代码

```java
public class ConsumerDemo {

    public static void consumeMsg(){
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("enable.auto.commit", true);       // 自动ofset
        props.put("auto.offset.reset", "earliest");  // 选取最开始的ofset作为起始读取位置
        props.put("group.id", "test");

        KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(props);
        kafkaConsumer.subscribe(Arrays.asList("test"));// 订阅消息


        while (true) {
            ConsumerRecords<String, String> records = kafkaConsumer.poll(Duration.ofMillis(100));
            System.out.println(records.count());
            for (ConsumerRecord<String, String> record : records) {
                System.out.println(String.format("topic:%s,offset:%d,消息:%s", record.topic(), record.offset(), record.value()));
            }
        }
    }
}
```

### 测试

测试的时候最好先开启消费者再开启生产者

### 关闭控制台打印的debug日志

kafka的api再使用时会自动打印很多的日志信息，可能会影响到观察业务的调试信息，下面介绍一种通过`logback`的方法关闭kafka api自带的日志打印

logback是一种日志管理工具，使用它需要再maven中配置依赖：

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-core</artifactId>
    <version>1.2.11</version>
</dependency>
```

然后在项目的resources目录下新建一个`logback.xml`，编写：

```xml
<?xml version="1.0" encoding="UTF-8"?>

<configuration>
    <logger name="org.apache.kafka" level="off" />
</configuration>
```

其含义就是关闭`org.apache.kafka`相关的一些日志输出

重新启动程序就可以看到debug信息没有了
