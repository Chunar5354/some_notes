毕业设计时用到的，写了很多代码，一直没有整理，陆续把一些用到的知识点写在这里

## 安装
在树莓派上的安装：`sudo apt-get install python3-pyqt5`
在windows上安装：`pip install pyqt5`

## 通常使用格式
一般会使用类的方式来进行QT的编程，格式通常是这样滴
```python
import sys
from PyQt5.QtWidgets import #这个库非常常用，很多常用方法来自于QtWidgets类

class QTtest(QWidget): #程序中创建的类要继承QWidget类
    def __init__(self):
        super().__init__() #继承类方法
        self.initUI() #定义初始函数，直接运行

    def initUI(self):
        #1.先把需要的元素构建出来

        #2.为按钮创建关联，一般关联在自定义的函数

        #3.对元素进行布局

        #4.进行显示
        self.setLayout(mainLayout) #在窗口显示
        self.setWindowTitle('Test')
        self.show() #显示三件套

    def printText(self): #自定义的处理函数


if __name__ == '__main__': #这个也是通常的调用三件套
    app = QApplication(sys.argv)
    ex = QTtest()
    sys.exit(app.exec_())

```

## 几种窗口

- Qt.Widget,默认窗口，有最小化、最大化、关闭按钮。
- Qt.Window,普通窗口，有最小化、最大化、关闭按钮。
- Qt.Dialog,对话框窗口，有问号和关闭按钮
- Qt.Popup,弹出窗口，窗口无边框
- Qt.ToolTip,提示窗口，窗口无边框，无任务栏
- Qt.SplashScreen,闪屏，窗口无边框，无任务栏
- Qt.SubWindow,子窗口，窗口无按钮，但有标题。

## QLineEdit一些知识点

- 设置文本初始选中：`selectAll()`
- 设置光标的初始位置：`setFocus()`
注意setFocus方法必须在控件显示之后使用，比如在setLayout之后
- 设置文本对齐方式：`setAlignment()`，有几种可选参数
  - Qt.AlignLeft：水平方向靠左对齐
  - Qt.AlignRight：水平方向靠右对齐
  - Qt.AlignCenter：水平方向居中对齐
  - Qt.AlignJustify：水平方向调整间距两端对齐
  - Qt.AlignTop：垂直方向靠上对齐
  - Qt.AlignBottom：垂直方向靠下对齐
  - Qt.AlignVCenter：垂直方向居中对齐
