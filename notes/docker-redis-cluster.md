## 配置redis集群

首先编辑一个redis配置模板文件`redis-cluster.tmpl`：

```
port ${PORT}
requirepass 1234
masterauth 1234
protected-mode no
daemonize no
appendonly yes
cluster-enabled yes
cluster-config-file nodes-conf
cluster-node-timeout 15000
cluster-announce-ip 1.15.140.88
cluster-announce-port ${PORT}
cluster-announce-bus-port 1${PORT}
```

创建配置文件，为端口号6701到6706各自创建一个配置文件

```
$ for port in `seq 6701 6706`; do\
    mkdir -p ${port}/conf \
    && PORT=${port} envsubst < redis-cluster.tmpl > ${port}/conf/redis.conf \
    && mkdir -p ${port}/data;\
done 
```

创建容器，基于上面六个配置文件创建6个容器

```
$ for port in $(seq 6701 6706); do \
    sudo docker run -di --restart always --name redis-${port} --net host \
    -v /home/chunar/docker-redis/redis-cluster/${port}/conf/redis.conf:/usr/local/etc/redis/redis.conf \
    -v /home/chunar/docker-redis/redis-cluster/${port}/data:/data \
    redis redis-server /usr/local/etc/redis/redis.conf; \
done
```

随意进入一个容器，通过redis命令创建redis集群

```
$ redis-cli -a 1234 --cluster create your_ip:6701 your_ip:6702 your_ip:6703 your_ip:6704 your_ip:6705 your_ip:6706 --cluster-replicas 1
```

`--cluster-replicas 1`用于指定集群为主从模式，每个主节点有一个从节点，前面三个是主节点，后面三个是从节点

以集群模式启动redis需要加上`-c`参数

```
$ redis -c -a 1234 -h your_ip -p 6701
```

## docker compose

docker compose是`批量`创建容器的编排工具，通过`.yml`文件来进行配置

以创建nginx容器为例，编辑一个`docker-compose.yml`文件：

```yml
# docker-compose的版本
version: "3.9"

# 在docker-compose中，每个容器都承载一个服务
services:
    nginx:  # 服务名称
        image: nginx  # 源自哪个镜像
        container_name: mynginx  # 容器名称
        ports:  # 端口映射
            - "80:80"
        networks:  # 网络模式
            - nginx-net

# 自建网络模式
networks:
    nginx-net:
        name: nginx-net
        driver: bridge  # 基于哪个基础网络模式
```

然后在当前路径下，输入下面的命令就会自动创建网络并开启容器：

```
$ docker-compose up
```

然后输入下面的命令可以自动删除网络与容器：

```
$ sudo docker-compose down
```

## docker swarm

建立swarm集群需要开启以下几个端口：

- TCP/2377，用于集群管理通信

- TCP,UDP/7946，用于节点通信

- UDP/4789，用于覆盖网络

新建集群：

```
$ sudo docker swarm init --advertise-addr your_ip
```

`--advertise-addr`指定当前机器的IP地址

创建成功后会打印出类似下面的信息：

```
Swarm initialized: current node (faqxk8nonfcf2a954p4z76gra) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-684733vfvtv33tcn4ttf5xkz0o3drua6s5j0v0s823jmffjfqp-b7obprvoxpii0jjwbqzo9p6b9 your_ip:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

它告诉我们：当前的节点默认成为一个`leader`，如果要向这个集群中添加`manager`或`worker`，需要带上集群的token

添加worker和manager节点的命令是不一样的，可以通过下面的命令来查看：

```
$ docker swarm join-token manager  // 查看添加manager节点的命令
$ docker swarm join-token worker   // 查看添加worker节点的命令
```

此时在管理节点中任意开启一个`服务`，以nginx为例

```
$ sudo docker service create --replicas 1 --name mynginx -p 80:80 nginx
```

然后在浏览器输入任意一个节点的IP地址，都可以连接到nginx页面，也就实现了集群部署

上面的命令中`--replicas 1`指的是只在一个节点上创建服务，也可以指定多个，或者在创建之后通过下面的命令更新：

```
$ sudo docker service update --replicas 2 mynginx
```

还可以通过以下命令进行查看：

```
$ sudo docker service ls  // 查看当前集群有哪些服务
$ sudo docker service ps service_name  // 查看某个服务运行在哪些节点上
$ sudo docker node ls   // 查看当前集群有哪些节点
```

以及删除节点：

```
$ sudo docker swarm leave           // 节点必须先leave才能被删除
$ sudo docker swarm leave --force   // manager节点需要带上--force参数
$ sudo docker node rm node_ID
```

### 弹性部署

docker swarm还提供了简便的方法用于快速部署和销毁多个服务:

```
$ sudo docker service scale service_name=2
```

通过scale在服务流量很大时可以迅速扩容，在流量小的时候也可以迅速删除多余的节点，实现弹性部署

注意一个节点上可以运行`多个同样的服务`
