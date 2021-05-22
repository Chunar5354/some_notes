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
