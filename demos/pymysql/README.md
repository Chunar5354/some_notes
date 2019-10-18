使用python中的pymysql模块操作mysql数据库
[参考文章](https://mp.weixin.qq.com/s/OM8U4rTJBm17Ey0nNxPCZg)

## 安装

- 树莓派上：`pip3 install pyMySQL`

## 主要方法

### connect()对象

使用示例：
```python
import pymysql

conn = pymysql.connect(host='localhost', 
                       user='root', 
                       port=3306, 
                       password='your_passwd',
                       database='test',
                       charset='utf8')
```

使用该方法与数据建立连接，各个参数：
- host：连接的mysql主机
- user：mysql用户
- port：连接的端口
- password：密码
- database：要连接的数据库
- charset：编码方式，默认为gb2312

connect()对象的方法：
- close()：关闭连接
- commit()：提交操作，只有提交了操作才会执行
- rollback()：放弃之前的操作
- cursor()：返回cursor对象，用于执行sql语句并返回结果

### cursor()对象

使用示例：
```python
import pymysql

conn = pymysql.connect(host='localhost', 
                       user='root', 
                       port=3306, 
                       password='your_passwd',
                       database='test',
                       charset='utf8')

cur = conn.cursor()

sql1 = "select * from pet where sex='f'"
count = cur.execute(sql1)
```

cursor()对象的方法：
- close()：关闭
- execute(sql[, parameters])：执行语句，返回受影响的行数
  - 可以在sql字符串后面带参数，修改具体操作的内容
- fetchone()：查询结果的第一行数据，返回一个元组
- next()：查询当前行的下一行
- fetchall()：查询数据的所有行，返回一个元组
- scroll(value[,mode])：将行指针移动到某个位置
  - value表示移动的行数
  - mode表示移动的方式，`relative`表示相对当前行移动多少行；`absolute`表示移动到绝对的行数位置
  

### 大量数据的插入操作

如果有大量数据需要存入数据库，可以使用pymysql.cursor中的`executemany()`方法，使用示例：

```python
sql = "INSERT INTO tablename(create_time, value) VALUES(%s, %s)"  # sql语句中要为datalist留出位置
datalist = [(create_time1, value1), (create_time1, value1), ...]  # datalist是一个要插入到数据库中的数据元组的列表（或元组）
count = cursor.executemany(sql, datalist)  # 插入数据，需要两个参数——sql语句和对应的数据元组列表
conn.commit()  # 提交执行命令
```

在数据量很大时，使用`executemany()`要比循环执行单次插入操作速度快得多

## pymysql+pandas读取数据库

有时单独使用pymysql来读取数据库中的某些数据会有部分丢失（比如读取精确到毫秒的时间），如果想要完整的读取数据库中的内容，可以借助pandas来实现

pandas中的`read_sql()`方法可以读取数据库中的数据，并保存成pandas.dataframe格式。[详情查看官方文档](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html)

dataframe对象可以后续通过一系列方法进行格式转换（如本例中的转换成列表）

应用示例：
```python
import pymysql
import pandas as pd
import numpy as np

db = pymysql.connect(host='',
		     user='username',
		     password='password',
		     database='db_name',
		     port=3306)
		     
sql = "select * from your_table"

# read_sql()最少接收两个参数，第一个是字符串格式的sql语句，第二个是数据库对象，返回结果是一个pandas.dataframe对象
result = pd.read_sql(sql, db)

# dataframe中的数据可以使用astype()强制转换类型，也可以通过result['column1']来为单个列的数据转换类型
result = result.astype(str)

# 使用numpy的array和tolist方法将dataframe对象转换成列表
num_result = np.array(result)
list_result = num_result.tolist()
```

## pymysql + threading多线程的问题

pymysql如果多线程公用一个数据库连接会出错，解决方法：

- 1.线程锁
- 2.每一个线程单独使用一个数据库连接
