pyqtgraph也是一个绘图的库，但是它与pyqt的兼容性非常好，能够绘制一些实时性比较高的图像

## 安装
在windows安装很简单：
- `pip install pyqtgraph`

树莓派上安装比较麻烦，使用pip的话会卡在配置numpy上，使用apt-get的话会强制一起安装pyqt4，与pyqt5的使用会有一些冲突  
好在pyqtgraph是完全的python文件，可以直接克隆其github上的文件到本地来调用
- 在项目目录下：`git clone https://github.com/pyqtgraph/pyqtgraph`
- 进入`pyqtgraph`目录：`python setup.py install`
- 然后可以将pyqtgraph当做本地的类进行调用
