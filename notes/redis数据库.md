* [安装](#%E5%AE%89%E8%A3%85)
  * [CentOS系统中](#centos%E7%B3%BB%E7%BB%9F%E4%B8%AD)
* [设置](#%E8%AE%BE%E7%BD%AE)
  * [密码登录](#%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95)
* [Python中的redis模块](#python%E4%B8%AD%E7%9A%84redis%E6%A8%A1%E5%9D%97)
  * [安装](#%E5%AE%89%E8%A3%85-1)
  * [基础用法](#%E5%9F%BA%E7%A1%80%E7%94%A8%E6%B3%95)
  * [连接池](#%E8%BF%9E%E6%8E%A5%E6%B1%A0)
  * [hash操作](#hash%E6%93%8D%E4%BD%9C)
  * [定时](#%E5%AE%9A%E6%97%B6)

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
print(res)
```

### 连接池

除了使用`redis.Redis()`方法进行连接之外，redis还提供了一种连接池的方法，可以为多个操作共享同一个数据库连接：
```python
# 创建一个连接池
pool = redis.ConnectionPool(host='localhost', port=6379, password='', db=0)
# 使用连接池进行连接
conn = redis.Redis(connection_pool=pool)
```

### hash操作

因为在实际使用的时候主要使用了hash存储，所以记录在这里，更多的redis操作[参考](https://segmentfault.com/a/1190000015191422)

- 1.插入： `hset(name, key, value)`
```python
conn.hset(hash_name, hash_key, hash_value)
# 注意因为redis中的数据都是以字节形式存储，所以各个参数的数据类型不能是列表或字典等
```

- 2.读取： `hget(name, key)`
```python
conn.hget(hash_name, hash_key)
# 结果为对应的hash_value
```

- 3.获取所有内容： `hgetall(name)`
```python
res = conn.hgetall(hash_name)
# 会返回hash_name中的所有键值对， res是一个字典
```

- 4.获取所有键： `hkeys(name)`
```python
res = conn.hkeys(hash_name)
# 返回hash_name中所有的键，res是一个列表
```

### 定时

redis有一个功能是可以为数据设置过期时间来节省内存，python的redis也同样可以实现这一操作：
```python
conn.expire(name, time)
# name为被设置的key或hash_name，注意不可以为hash中的hash_key单独设置过期时间
# time可以是整数，单位为秒；或者可以是datetime格式化的时间
```


## 内存淘汰

在reids中。除了设置过期时间来清理数据，还可以通过它的内存淘汰机制。即当redis中的数据占用内存超过设置数值时，删除某些数据来释放内存。

redis有六种内存淘汰策略，详细信息可以[参考](https://www.jianshu.com/p/c8aeb3eee6bc)，通常使用的为`allkeys-lfu`或`allkeys-lru`

- allkeys-lfu: 清除所有键中使用频率最低的键
- allkeys-lru: 清除所有键中最久没有使用的键

设置方法为：针对Centos系统，修改`/etc/redis/redis.conf`文件，修改下面两行
```
maxmemory 256mb                   # 设置内存上限
maxmemory-policy allkeys-lfu      # 设置内存淘汰策略
```
