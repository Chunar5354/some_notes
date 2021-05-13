## 安装

### Docker容器

```
$ docker pull elasticsearch:version
```

在运行elasticsearch容器时，可能会出现一些错误：

- 错误1

```
ERROR: [1] max virtual memory areas vm.max_map_count [65530] likely too low, increase to at least [262144]
```

原因是为虚拟机分配的内存不足，通过

```
$ sysctl -w vm.max_map_count=262144
```

修改

如果是在windows上使用docker，则首先要通过WSL连接到虚拟机

```
$ wsl -d docker-desktop
$ sysctl -w vm.max_map_count=262144
```

- 错误2

```
ERROR: [1] bootstrap checks failed. You must address the points described in the following [1] lines before starting Elasticsearch.
bootstrap check failure [1] of [1]: the default discovery settings are unsuitable for production use; at least one of [discovery.seed_hosts, discovery.seed_providers, cluster.initial_master_nodes] must be configured
```

这种情况是因为某些环境变量没有配置好，需要在运行容器的时候加上环境变量参数，如：

```
$ docker run --name my_es -e ES_JAVA_OPTS="-Xms256m -Xmx256m"  -e "discovery.type=single-node" -d -p 9200:9200 -p 9300:9300 elasticsearch:7.12.1
```

然后就可以在`http://localhost:9200`查看结果

## 使用

elasticsearch默认使用9200端口，并且遵循RESTFUL规范，可以在浏览器上输入`http://localhost:9200`查看

elasticsearch类似于数据库，其中的库在es中称为`Index`，表称为`Type`，表中的数据以Id标识

### 添加数据

通过REST工具发送下面的报文，就相当于在Index为test，Type为chunar，Id为1的一条数据，包含name和value两个字段

```
POST http://localhost:9200/test/chunar/1
Content-Type: application/json

{
    "name": "chunar",
    "value": "123456"
}
```

### 查询数据

- 查询所有记录

```
GET http://localhost:9200/_cat/indices
```

- 查询某个表中的所有数据

```
GET http://localhost:9200/<your_index>/<your_type>/_search
```

- 查询某条数据

```
GET http://localhost:9200/<your_index>/<your_type>/<your_id>
```

### 删除数据

- 删除某个Index中的全部数据

```
POST http://localhost:9200/<your_index>/_delete_by_query
Content-Type: application/json

{"query":{"match_all":{}}}
```
