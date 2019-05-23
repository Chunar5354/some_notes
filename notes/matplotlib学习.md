## 基本用法

树莓派上安装：`sudo apt-get install python3-matplotlib`

```python
import matplotlib.pyplot as plt
import numpy as np

#开启一个窗口，num设置子图数量，figsize设置窗口大小，dpi设置分辨率
fig = plt.figure(num=1, figsize=(15, 8),dpi=80)
#直接用plt.plot画图，第一个参数是表示横轴的序列，第二个参数是表示纵轴的序列
plt.plot(np.arange(0,1,0.1),range(0,10,1)) #同一个窗口绘制多条曲线
plt.plot(np.arange(0,1,0.1),range(0,20,2))
#显示绘图结果
plt.show()

```

```python
import matplotlib.pyplot as plt
import numpy as np

#开启一个窗口，num设置子图数量，这里如果在add_subplot里写了子图数量，num设置多少就没影响了
#figsize设置窗口大小，dpi设置分辨率
fig = plt.figure(num=2, figsize=(15, 8),dpi=80)
#使用add_subplot在窗口加子图，其本质就是添加坐标系
#三个参数分别为：行数，列数，本子图是所有子图中的第几个，最后一个参数设置错了子图可能发生重叠
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
#绘制曲线
ax1.plot(np.arange(0,1,0.1),range(0,10,1),color='g')
#同理，在同一个坐标系ax1上绘图，可以在ax1坐标系上画两条曲线，实现跟上一段代码一样的效果
ax1.plot(np.arange(0,1,0.1),range(0,20,2),color='b')
#在第二个子图上画图
ax2.plot(np.arange(0,1,0.1),range(0,20,2),color='r')
plt.show()

```

## 在PyQt界面中添加matplotlib图像

需要借助matplotlib中的FigureCanvas类，在PyQt界面中生成一个画布控件，首先import这个方法：
```python
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure #用于创建画布对象
import matplotlib.pyplot as plt
```

然后新建一个类，继承FigureCanvas方法：
```python
class PlotTri(FigureCanvas):
    def __init__(self, parent=None, width=7, height=4, dpi=100): #定义尺寸和分辨率
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
```

之后可以在主窗口中将自定义的画图类实例化，调用其中的绘图方法：
```python
self.m = PlotTri(self, width=7, height=4) #实例化绘图方法
# self.m可以像其他窗口控件一样进行布局与关联槽函数
```

## 设置坐标轴

### 针对用pyplot绘制的图像

```python
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-2, 2))
#设置坐标轴名称
plt.xlabel('x')
plt.ylabel('y')
#设置坐标轴刻度
my_x_ticks = np.arange(-5, 5, 0.5)
my_y_ticks = np.arange(-2, 2, 0.2)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
```

### 针对使用figure绘制的图像

```python

# 设置坐标轴范围
self.axe1.set_xlim((0, 20))
self.axe2.set_xlim((0, 20))
self.axe3.set_xlim((0, 20))
self.axe1.set_ylim((0, 15))
self.axe2.set_ylim((0, 15))
self.axe3.set_ylim((0, 15))

# 设置坐标轴名称
self.axe1.set_xlabel('time')
self.axe1.set_ylabel('voltage /V')
self.axe2.set_xlabel('time')
self.axe2.set_ylabel('electricity /A')
self.axe2.set_xlabel('time')
self.axe3.set_ylabel('voltage')

# 在图像的任意位置添加文字
# 参数分别对应（x轴位置，y轴位置，文本内容，垂直对齐方式，水平对齐方式）
self.axe1.text(21.3, 0.01, 'time',
verticalalignment='bottom', horizontalalignment='right')

self.axe2.text(21.3, 0.01, 'time',
verticalalignment='bottom', horizontalalignment='right')

self.axe3.text(21.3, 0.01, 'time',
verticalalignment='bottom', horizontalalignment='right')
