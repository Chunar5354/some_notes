看到crossing教室的`图像风格迁移`的介绍，感觉很有趣，就copy了一个，顺便学了一下opencv

- 我用的是cv2，首先需要安装：`pip install opencv-python`
- 通过命令行打开图像窗口想退出的时候，不要点窗口上的关闭，会导致命令行出错，直接按`Esc`即可

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

## 对图像进行处理

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

## 添加文字

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
