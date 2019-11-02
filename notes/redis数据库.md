## 安装

### CentOS系统中

首先添加`EPEL`源，更新yum：
```
$ sudo yum install epel-release
$ sudo yum update
```

安装redis：
```
$ sudo yum install redis -y
```

通过系统服务来启动redis：
```
$ sudo systemctl start redis
```

redis的配置文件为`/etc/redis/redis.conf`，要想redis在后台启动，需要将配置文件中的
```
daemonize no
```
一行修改为:
```
daemonize yes
```

服务启动后，可以通过下面的命令来打开客户端：
```
$ redis-cli
```

## 设置

### 密码登录

修改配置文件`/etc/redis/redis.conf`，将其中的：
```
#requirepass foobared
```
去掉注释，并在requirepass后添加自定义的密码：
```
requirepass your_password
```

然后重启redis生效

- 如果要带密码启动客户端，需要加上`-a`参数
```
$ redis-cli -a your_password
```

- 也可以直接启动，在redis中通过`auth`语句重新输入密码
```
$ redis-cli
127.0.0.1:6379> auth your_password
OK
```

## Python中的redis模块

使用redis扩展包可以通过python操作redis。[官网链接](https://pypi.org/project/redis/)

### 安装

```
# pip install redis
```

### 基础用法

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
res = r.get('foo')
print(res
```
