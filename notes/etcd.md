## 安装

### Linux环境

[官方](https://etcd.io/docs/v3.4/quickstart/#install-etcd)给出了一个安装脚本，但是由于外网的原因，可能下载速度很慢

可以在ectd的github上找到最新版本的[release压缩包](https://github.com/etcd-io/etcd/releases)

下载并解压，然后将解压后文件夹中的`etcd`和`etcdctl`复制到`GOBIN`中，测试：

```
$ etcd --version
etcd Version: 3.4.16
Git SHA: d19fbe541
Go Version: go1.12.17
Go OS/Arch: linux/amd64
```

```
$ etcdctl version
etcdctl version: 3.4.16
API version: 3.4
```

- 运行测试

测试etcd需要在一个终端通过`etcd`命令开启服务，在另一个终端通过`etcdctl`连接服务

### docker

etcd没有官方镜像，但有两个比较火的镜像bitnami和elcolio，以bitnami为例

拉取镜像：

```
$ docker pull bitnami/etcd
```

运行：

```
$ docker run --name my_etcd -p 2379:2379 -p 2380:2380 -e ALLOW_NONE_AUTHENTICATION=yes -d bitnami/etcd
```

## 集群启动

[参考](http://blueskykong.com/tags/etcd/)

### Docker方式启动集群

以bitnami镜像为例

shell脚本

```sh
#!/bin/bash

#新建网络名
network_name=etcd_network

#创建网络
sudo docker network create --driver bridge --subnet=172.22.0.0/16 --gateway=172.22.0.1 ${network_name}

#设置结点名
node1=etcd_node1
node1_ip=172.22.0.2

node2=etcd_node2
node2_ip=172.22.0.3

node3=etcd_node3
node3_ip=172.22.0.4

#设置集群口令
cluster_token=etcd_cluster


#创建节点1
sudo docker run -d --name ${node1} \
	--network ${network_name} \
	--publish 12041:2379 \
	--publish 12051:2380 \
	--ip ${node1_ip} \
	--env ALLOW_NONE_AUTHENTICATION=yes \
	--env ETCD_NAME=${node1} \
	--env ETCD_ADVERTISE_CLIENT_URLS=http://${node1_ip}:2379 \
	--env ETCD_INITIAL_ADVERTISE_PEER_URLS=http://${node1_ip}:2380 \
	--env ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
	--env ETCD_LISTEN_PEER_URLS=http://0.0.0.0:2380 \
	--env ETCD_INITIAL_CLUSTER_TOKEN=${cluster_token} \
	--env ETCD_INITIAL_CLUSTER=${node1}=http://${node1_ip}:2380,${node2}=http://${node2_ip}:2380,${node3}=http://${node3_ip}:2380 \
	--env ETCD_INITIAL_CLUSTER_STATE=new \
	bitnami/etcd:latest

#创建节点2
sudo docker run -d --name ${node2} \
	--network ${network_name} \
	--publish 12042:2379 \
	--publish 12052:2380 \
	--ip ${node2_ip} \
	--env ALLOW_NONE_AUTHENTICATION=yes \
	--env ETCD_NAME=${node2} \
	--env ETCD_ADVERTISE_CLIENT_URLS=http://${node2_ip}:2379 \
	--env ETCD_INITIAL_ADVERTISE_PEER_URLS=http://${node2_ip}:2380 \
	--env ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
	--env ETCD_LISTEN_PEER_URLS=http://0.0.0.0:2380 \
	--env ETCD_INITIAL_CLUSTER_TOKEN=${cluster_token} \
	--env ETCD_INITIAL_CLUSTER=${node1}=http://${node1_ip}:2380,${node2}=http://${node2_ip}:2380,${node3}=http://${node3_ip}:2380 \
	--env ETCD_INITIAL_CLUSTER_STATE=new \
	bitnami/etcd:latest

#创建节点3
sudo docker run -d --name ${node3} \
	--network ${network_name} \
	--publish 12043:2379 \
	--publish 12053:2380 \
	--ip ${node3_ip} \
	--env ALLOW_NONE_AUTHENTICATION=yes \
	--env ETCD_NAME=${node3} \
	--env ETCD_ADVERTISE_CLIENT_URLS=http://${node3_ip}:2379 \
	--env ETCD_INITIAL_ADVERTISE_PEER_URLS=http://${node3_ip}:2380 \
	--env ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
	--env ETCD_LISTEN_PEER_URLS=http://0.0.0.0:2380 \
	--env ETCD_INITIAL_CLUSTER_TOKEN=${cluster_token} \
	--env ETCD_INITIAL_CLUSTER=${node1}=http://${node1_ip}:2380,${node2}=http://${node2_ip}:2380,${node3}=http://${node3_ip}:2380 \
	--env ETCD_INITIAL_CLUSTER_STATE=new \
	bitnami/etcd:latest
```

参数说明：

- `--env ALLOW_NONE_AUTHENTICATION`，不进行验证

- `--env ETCD_NAME`，设置成员节点别名

- `--env ETCD_ADVERTISE_CLIENT_URLS`，本节点监听的客户端地址

- `--env ETCD_INITIAL_ADVERTISE_PEER_URLS`，节点成员间通信地址

- `--env ETCD_LISTEN_CLIENT_URLS`，节点监听的客户端通信地址

- `--env ETCD_LISTEN_PEER_URLS`，监听的用于节点通信的地址

- `--env ETCD_INITIAL_CLUSTER_TOKEN`，指定集群口令，拥有相同token的节点才能加入同一个集群

- `--env ETCD_INITIAL_CLUSTER`，所有节点的地址列表

### 以动态发现方式启动集群

应用于节点IP地址未知的情况

原理是以来另一个etcd集群，在该集群中创建一个目录，在该目录中创建一个_config子目录，在子目录中增加size节点，指定新集群的节点数目

- 基于公共discovery

首先向公共`discovery.etcd.io`申请token(集群有几个节点size就填几)，然后会得到一个地址：

```
$ curl -w "\n" 'https://discovery.etcd.io/new?size=2'
https://discovery.etcd.io/edc2dbac966c7a2475dd35cdc14f76fc
```

然后使用脚本创建docker容器（注意倒数第二行的改动）：

```sh
#!/bin/bash

#设置结点名
node1=etcd_node1
node1_ip=172.22.0.2

node2=etcd_node2
node2_ip=172.22.0.3

dir="/var/lib/etcd"
discovery="https://discovery.etcd.io/edc2dbac966c7a2475dd35cdc14f76fc"

#创建节点1
sudo docker run -d --name ${node1} \
	--publish 12041:2379 \
	--publish 12051:2380 \
	--env ALLOW_NONE_AUTHENTICATION=yes \
	--env ETCD_NAME=${node1} \
    --env ETCD_DATA_DIR=${dir} \
	--env ETCD_ADVERTISE_CLIENT_URLS=http://${node1_ip}:12041 \
	--env ETCD_INITIAL_ADVERTISE_PEER_URLS=http://${node1_ip}:12051 \
	--env ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
	--env ETCD_LISTEN_PEER_URLS=http://0.0.0.0:2380 \
	--env ETCD_DISCOVERY=${discovery} \
	bitnami/etcd:latest

#创建节点2
sudo docker run -d --name ${node2} \
	--publish 12379:2379 \
	--publish 12380:2380 \
	--env ALLOW_NONE_AUTHENTICATION=yes \
	--env ETCD_NAME=${node2} \
    --env ETCD_DATA_DIR=${dir} \
	--env ETCD_ADVERTISE_CLIENT_URLS=http://${node2_ip}:12379 \
	--env ETCD_INITIAL_ADVERTISE_PEER_URLS=http://${node2_ip}:12380 \
	--env ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379 \
	--env ETCD_LISTEN_PEER_URLS=http://0.0.0.0:2380 \
	--env ETCD_DISCOVERY=${discovery} \
	bitnami/etcd:latest
```

通过`--env ETCD_DISCOVERY`指定了动态发现的token

## etcdctl操作

etcdctl是etcd自带的命令行客户端，提供了一些简洁的API
