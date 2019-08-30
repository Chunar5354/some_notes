想参加数模比赛，要用到数学模型和科学计算一些东西，Python中有很多支持数据处理的库，一点一点的记录在这里

## pandas

- 安装：
  - pip安装：`pip3 install pandas`
  - apt-get安装：`apt-get install python-pandas`

pandas的全称为pannel data analysis（面板数据分析），是一个基于numpy的库，在Python内置数据结构的基础上，pandas中有两种独特的数据结构：`Series`和`DataFrame`。

### Series

Series可以理解为一个`带索引值`的列表：
```python
import pandas as pd

x = pd.Series([1, 2, 3, 4])
print('Type is: \n', type(x))
print('X is: \n', x)
print('x.index is: \n', x.index)
print('x.values is: \n', x.values)
```

运行这段程序，输出结果为：
```
Type is:
 <class 'pandas.core.series.Series'>
X is:
 0    1
1    2
2    3
3    4
dtype: int64
x.index is:
 RangeIndex(start=0, stop=4, step=1)
x.values is:
 [1 2 3 4]
```

其中，Series的值不仅可以是数字，也可以是字符串、列表等其他对象：
```python
x = pd.Series(['1, 2, 3, 4', '22', 123, 'asc', [1,2]])       # 这些都是可行的
```

也可以在创建Series时`自定义其索引值`：
```python
import pandas as pd

x = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'd', 'c'])
print('Type is: \n', type(x))
print('X is: \n', x)
print('x.index is: \n', x.index)
print('x.values is: \n', x.values)
```

此时输出结果变成（注意index的变化）：
```
Type is:
 <class 'pandas.core.series.Series'>
X is:
 a    1
b    2
d    3
c    4
dtype: int64
x.index is:
 Index(['a', 'b', 'd', 'c'], dtype='object')
x.values is:
 [1 2 3 4]
```

- 待续

### DataFrame

把Series当作一维数组的话，DataFrame就相当于二维数组，它具有行列，类似于数据库

- 待续

## cufflinks

cufflinks是一个关于图像绘制的库，是在plotly的基础上做了包装改进，使用它可以绘制出很高端漂亮的数据图，它需要运行在`Jupyter notebook`中

[Jupyter notebook使用](https://github.com/Chunar5354/some_notes/blob/master/notes/Anaconda%E4%BD%BF%E7%94%A8.md)
[cufflinks简单教程](https://mp.weixin.qq.com/s/Ns-k-KIeLN23rPgCtlTiGw)


