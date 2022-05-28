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
* [php中操作redis](#php%E4%B8%AD%E6%93%8D%E4%BD%9Credis)
  * [安装扩展](#%E5%AE%89%E8%A3%85%E6%89%A9%E5%B1%95)
  * [代码示例](#%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B)
* [内存淘汰](#%E5%86%85%E5%AD%98%E6%B7%98%E6%B1%B0)


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

## 常用命令

### 删除

- 删除当前数据库中的所有key

```
flushdb
```

- 删除所有数据库中的key

```
flushall
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

## php中操作redis

### 安装扩展

- 1.下载源码包

php操作redis需要先安装扩展，在[这里](https://github.com/phpredis/phpredis/releases)找到最新版本的安装包下载，如：
```
# wget https://github.com/phpredis/phpredis/archive/5.1.1.tar.gz
```
然后解压，进入到文件目录下
```
# tar -zxvf 5.1.1.tar.gz
# cd phpredis-5.1.1
```

- 2.编译

然后先使用`phpize`编译，如果没有的话需要先安装phpize，以centos系统为例：
```
# sudo yum install php-devel
```
注意有可能安装了多个php（比如我有两个，一个在`/etc`路径下，一个在`/etc/opt/remi/php73/`路径下），则以下所有的php
相关的文件（`php.ini`, `phpize`, `php-config`）都有两份，要进行两次相同的操作，如果不确定自己的php安装路径可以通过`find`进行查找。

phpize编译
```
# /etc/opt/remi/php73/phpize
```

然后找到`php-config`的位置
```
# sudo find / -name php-config
```

进行编译
```
# ./configure --with-php-config=/opt/remi/php73/root/usr/bin/php-config
# sudo make
# sudo make install
```

- 3.修改配置

这里比较坑，网上大多数的说法是再php.ini文件中直接添加exension，但是这样会出错;

正确的做法是在`php.d`文件夹下创建新文件`redis.ini`，在`redis.ini`里加入`extension=redis.so`这行.

我这里是以`/etc/opt/remi/php73/`路径下的php为例，实际可能要在另一个路径下的php重复上面的操作。

- 4.重启apache

redis扩展已经配置完毕，重启服务
```
# sudo systemctl restart httpd.service
```

### 代码示例

可以参考这篇[文章](https://learnku.com/articles/22942)

简单测试：
```php
// 实例化redis
$redis = new Redis();
// 连接
$redis->connect('127.0.0.1', 6379);
// 通过密码连接
$redis->auth('password');
// 检测是否连接成功
echo "Server is running: " . $redis->ping();   // 输出结果 Server is running: +PONG 
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

## redis远程连接

redis默认是不允许远程连接的，需要修改配置文件，一般是`/etc/redis/redis.conf`

找到其中的

```
bind 127.0.0.1
```

将其修改为

```
bind *  # 为安全起见也可以改成固定的IP
```

然后重启redis

```
$ sudo systemctl restart redis
```

可以在另一台机器上进行测试：

```
redis-cli -h 目标IP -p 端口
```
