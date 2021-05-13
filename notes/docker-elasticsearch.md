使用docker容器启动ealsticsearch时，可能会报两个错误：

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
