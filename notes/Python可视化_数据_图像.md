想参加数模比赛，要用到数学模型和科学计算一些东西，Python中有很多支持数据处理的库，一点一点的记录在这里

## matplotlib

matplotlib是一个常用的功能强大的python图像绘制库，有丰富的图像类型和功能

基本使用方法：
```python
from matplotlib import pyplot as plt

x = [1, 3, 4, 5]
y = [i**2 for i in x]

plt.plot(x, y)
plt.show()
```

### 使用时的知识点

- 1.修改坐标轴标签的方向（在坐标轴密集的时候很有用）
```python
plt.xticks(rotation='vertical')   # 将x轴标签改为垂直方向
```

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

### 使用pandas绘制图像

#### 从文件中读取数据

pandas可以读取csv文件，并返回一个`DataFrame`对象：
```python
import pandas as pd

# read_csv can accept an encoding parament
# if the csv file was exported by Excel, use encoding='gb18030'
df = pd.read_csv('account.csv', encoding='gb18030')
```

可以通过columns属性来查看这个DataFrame包含了哪些列：
```python
print(df.columns)
```

会打印类似下面的内容，列表中是各个列的名称：
```
Index(['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6',
       'Column7'],
      dtype='object')
```

其中每一列对应一个Series对象：
```python
print(df['Column1'])
print(type(df['Column1']))
```

#### 图像绘制

在上一节得到了每一列之后，就可以通过`matplotlib`直接绘制图像：
```python
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('account.csv', encoding='gb18030')
x = df['Column1']
y = df['Column2']

plt.plot(x, y)
plt.show()
```

或者可以直接使用DataFrame对象的plot()方法来绘制图像（Series对象也可以）：
```python
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('account.csv', encoding='gb18030')
df.plot()
plt.show()
```

不过这样绘制出的图像x轴是自动生成的，修改起来比较麻烦


## cufflinks

cufflinks是一个关于图像绘制的库，是在plotly的基础上做了包装改进，使用它可以绘制出很高端漂亮的数据图，它需要运行在`Jupyter notebook`中

[Jupyter notebook使用](https://github.com/Chunar5354/some_notes/blob/master/notes/Anaconda%E4%BD%BF%E7%94%A8.md)
[cufflinks简单教程](https://mp.weixin.qq.com/s/Ns-k-KIeLN23rPgCtlTiGw)




