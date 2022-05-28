## 通过Java访问Redis

### Jedis依赖

再Java中访问Redis可以通过Jedis来实现

[官方网站](https://github.com/redis/jedis)

依赖需要通过maven管理，在项目的pom.xml中，添加：

```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>4.2.0</version>
</dependency>
```

### 使用示例

```java
public class RedisHandler {
    public void redisRun() {
        // 配置连接池
        JedisPoolConfig config = new JedisPoolConfig();
        config.setMaxTotal(20);
        config.setMaxIdle(10);
        config.setMinIdle(5);

        // 创建连接池
        JedisPool jedisPool = new JedisPool(config, "localhost", 6379);

        Jedis jedis = jedisPool.getResource();

        // 密码
        jedis.auth("password");
        // redis操作
        jedis.set("id", "123");
        String res = jedis.get("id");
        System.out.println(res);

        // 关闭连接
        jedis.close();
    }
}
```