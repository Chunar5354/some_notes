unix时间戳是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒（闰秒，是指为保持协调世界时接近于世界时时刻，由国际计量局统一规定在年底或年中（也可能在季末）对协调世界时增加或减少1秒的调整）。

使用unix时间戳可以统一时间，使得应用更好地跨平台使用

python中可以使用`time.time()`方法获得10位整数+小数形式的时间戳，也可以将其转换为`year-month-date hour:minute:second`形式的时间戳：

```python
import time

# 将小数格式转换为年月日格式
def timestamp_datatime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

# 将年月日格式转换成小数格式
def datatime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M'))
    return s
  
tim = time.time()
value = int(tim)
s = timestamp_datatime(value)
print(tim)
print(s)
```
