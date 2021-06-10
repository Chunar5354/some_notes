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

etcdctl是etcd自带的命令行客户端，提供了一些简洁的API，在此记录一些常用的操作

### 增删改查

- 添加键值对`put`

```
$ etcdctl put greeting 'hello world'
OK
```

- 通过键获取值`get`

```
$ etcdctl get greeting
greeting
hello world
```

- 只读取值`--print-value-only`

```
$ etcdctl get greeting --print-value-only
hello world
```

- 范围查询（区间）

先插入一组可排序的键：

```
$ etcdctl put test1 '123'
$ etcdctl put test2 '456'
$ etcdctl put test3 '789'
```

在查询时指定左右端点（`左闭右开`）

```
$ etcdctl get test1 test3
test1
123
test2
456
```

只要是可排序的键，在查找时都会输出出来，所以要谨慎选择键名

```
$ etcdctl put t '111'
```

可以从t开始排序

```
$ etcdctl get t test3
t
111
test1
123
test2
456
```

- 范围查询，查询大于等于某个键`byte值`的键 `--from-key`

```
$ etcdctl get --from-key test1
test1
123
test2
456
test3
789
```

- 前缀查询`--prefix`

```
$ etcdctl get --prefix te
test1
123
test2
456
test3
789
```

- 限制输出结果数量`--limit`

```
$ etcdctl get --prefix t --limit=2
t
111
test1
123
```

- 读取旧版本`--rev`

有时会对某个键的值进行修改，想查询之前的值可以通过指定历史版本来实现

在etcd中，版本0表示删除（墓碑），版本1表示键不存在，所以用户插入的版本从2开始

```
$ etcdctl put rev_test '1'     // 版本为2
$ etcdctl put rev_test '2'     // 版本为3
$ etcdctl put rev_test '3'     // 版本为4
```

```
$ etcdctl get rev_test           // 最新版本是3
rev_test
3

$ etcdctl get rev_test --rev=3   // 版本3对应的值是2
rev_test
2
```

为了防止版本太多占用空间，可以通过`compact`进行压缩，使得某个版本之前都不可访问

```
$ etcdctl compact 3
```

此时再访问3之前的版本就会报错

- 删除键`del`

```
$ etcdctl del rev_test
1
```

然后就查询不到该键，但是可以查到`历史版本`

```
$ etcdctl get rev_test
$ etcdctl get rev_test --rev=2
rev_test
1
```

### watch监视

通过watch来监视一个键，一旦发生更新（版本的更新，不是值的更新），就输出`更新的方法`和`更新后的键值对`

在一个终端：

```
$ etcdctl watch test1
```

另一个终端：

```
$ etcdctl put test1 '321'
```

监视的那个终端就会打印：

```
PUT
test1
321
```

即使改成相同的值也会监测到变化，再来一次：

```
$ etcdctl put test1 '321'
```

仍然会打印

```
PUT
test1
321
```

还可以查看自某个历史版本以来的所有改动

```
$ etcdctl watch --rev=2 rev_test
PUT
rev_test
1
PUT
rev_test
2
PUT
rev_test
3
```

### 租约

所谓租约就是给键设置一个`过期时间`，在租约到期时，租约以及附带的所有键都会被删除

首先创建一个租约，会得到一个租约ID

```
$ etcdctl lease grant 30
lease 694d79f5bb6c6e2e granted with TTL(30s)
```

然后可以将键附加到租约上，当租约到期后会一起删除

```
$ etcdctl put --lease=694d79f5bb6c6e2e test_lease '123'
```

查看当前的所有租约

```
$ etcdctl lease list
found 1 leases
694d79f5bb6c6e2e
```

查看某个租约的信息：

```
$ etcdctl lease timetolive 694d79f5bb6c6e34
lease 694d79f5bb6c6e34 granted with TTL(30s), remaining(22s)
```

刷新租约，会按照创建时的设定来`重置计时`

```
$ etcdctl lease keep-alive 694d79f5bb6c6e34
lease 694d79f5bb6c6e34 keepalived with TTL(30)
```
