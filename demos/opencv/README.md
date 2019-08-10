关于opencv库的学习

## 安装

### windows

```
pip install opencv-python
```
通过命令行打开图像窗口想退出的时候，不要点窗口上的关闭，会导致命令行出错，直接按`Esc`即可

### 树莓派

首先更新系统
```
sudo apt-get update 
sudo apt-get upgrade
```

安装opencv和numpy：
```
sudo pip3 install opencv-python imutils numpy scipy pillow
其他的一些库也是关于图像处理和科学计算，可以选择安装
```

安装依赖
```
sudo apt-get install libatlas-base-dev  libjasper-dev
sudo apt-get install libgstreamer1.0-0
sudo apt-get install libgstreamer-plugins-base1.0-0
sudo apt-get install libqtgui4  libqt4-test
```

然后就可以在解释器中`import cv2`测试，安装成功

- 注意树莓派要使用摄像头的话需要在`sudo raspi-config`中将摄像头打开并重启

- 为树莓派添加摄像头默认设备：

编辑配置文件
```
sudo vi/etc/modules-load.d/modules.conf
```
在其中添加一行：
```
bcm2835-v4l2
```
然后重启，就可以使用诸如`cv2.VideoCapture(0)`的方法来打开摄像头


## 基本操作

```python
import cv2

image = cv2.imread('target_picture.jpg', flags) # 读取一个图像对象
# 这里面的flags是读取图片时可以附带的参数
#flags =：
  #cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
  #cv2.IMREAD_GRAYSCALE：读入灰度图片
  #cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道

cv2.namedWindow('窗口名称') # 新建一个显示窗口
cv2.image('窗口名称', 图像对象名) # 在该窗口显示该图像
cv2.imwrite('目标写入路径', 图像对象名) # 保存图片

cv2.waitKey(0) # 加上这一句，否则无法正常显示
cv2.destroyAllWindows() # 最后关闭窗口
```

### 对图像进行处理

```python
import cv2
image = cv2.imread('target_picture.jpg')

shape_num = image.shape # 返回一个三元元组——（高，宽，通道）
cv2.resize(图像对象名, (高,宽), interpolation = flags) # 改变图像大小，参数需要是整数
# interpolation - 插值方法。共有5种：
  #１）INTER_NEAREST - 最近邻插值法
  #２）INTER_LINEAR - 双线性插值法（默认）
  #３）INTER_AREA - 基于局部像素的重采样（resampling using pixel area relation）。对于图像抽取（image decimation）来说，这可能是一个更好的方法。但如果是放大图像时，它和最近邻法的效果类似。
  #４）INTER_CUBIC - 基于4x4像素邻域的3次插值法
  #５）INTER_LANCZOS4 - 基于8x8像素邻域的Lanczos插值
```

### 添加文字

```python
import cv2
img = cv2.imread('target_picture')

font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
cv2.putText(img, '000', (50, 50), font, 1.2, (255, 255, 255), 2) #这里的参数先宽后高
# 各个参数：图像对象，文字内容，坐标，字体，大小，颜色，文字厚度

# 也可以把添加文字之后的图像创建一个新的对象：
img_write = cv2.putText(img, '000', (50, 50), font, 1.2, (255, 255, 255), 2)
# 不过就算创建了新的对象，原来的img对象也已经被修改了
# 如果想保留原来的对象，就要在putText之前加上一句备份：
img_copy = img.copy() # 创建一个img的备份对象
```

## 实时显示拍摄视频

代码如下
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    # capture frame-by-frame
    ret, frame = cap.read()
    frame1 = cv2.flip(frame, -1)  # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Change color

    cv2.imshow('frame', frame1)  # Display 1
    cv2.imshow('gray', gray)     # Display 2

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

# when everything done , release the capture
cap.release()
cv2.destroyAllWindows()
```

运行这部分代码，会看到一正一反，一彩色一灰色两个视频

## 远程监控

### 踩的一些坑

远程视频监控总体可分成3步：

- 1.源视频端摄像头录制视频，将图片一帧帧上传到服务器
- 2.服务器开启相应端口与数据接收、转发功能
- 3.客户端连接服务器，获取视频数据，解码并播放

这就涉及到几个问题：

- 1.数据的传输打算使用socket来实现，socket传输接受的是`字节`数据，而使用opencv创建的图片格式为`numpy.ndarray`格式，所以需要转换数据格式
- 2.图片的尺寸太大，增加传输负担，需要`压缩`

中间尝试了许多办法，最后参考[这篇文章](https://www.jianshu.com/p/4aed39710676)成功了

各种坑：

- 1.最开始使用`StringIO()`方法开辟缓存一读一写来转码，但是StringIO()只支持写入`字符串`，将图片信息强行转换为字符串会丢失信息，所以失败了
- 2.想使用`tostring()`方法直接将`numpy.ndarray`的图片转换为字节串：`img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).tostring()`，使用socket发送，再从接收端获取字节串，使用`mp.frombuffer()`将字节串再变成`numpy.ndarray`；但是这样出现一个问题：原本图片中的array是一个像素矩阵，但是使用tostring格式化之后再解码，就变成了一个数字列表，丢失了原来的图片格式信息，所以又失败了
- 3.后来又找到了一个pickle打包的方式，调用`_pickle`模块：`import _pickle as pickle`，使用`pickle.dumps()`方法将图片打包成字节串，再从客户端上使用`pickle.loads()`解包成numpy.ndarray，格式对得上但是会触发未知错误，再次失败
- 4.最后是使用的`struct.pack()`与`struct.unpack()`方法实现的格式转换

## 人脸识别

人脸识别是一个机器学习相关的应用，需要训练分类器，opencv提供了训练分类器的方法

也可以从[这里](https://github.com/opencv/opencv/tree/master/data/haarcascades)找到一些训练好的分类器
