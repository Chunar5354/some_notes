毕业设计要写用户界面，感觉tkinter有点丑，学习一下pyqt库，看看是不是一个好的选择

在树莓派上的安装：`sudo apt-get install python3-pyqt5`

## 关于引用
这个库的引用比较麻烦，因为其中有好多函数：

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

## 借了本书
借了一本关于PyQt编程的书，是PyQt4版本的，有一点小出入，可以百度查到
根据书上的例子写一些例程，笔记都写在程序的注释里面了
从19-3-8开始

## 陆续加点东西

PyQt5几种窗口风格
- Qt.Widget,默认窗口，有最小化、最大化、关闭按钮。
- Qt.Window,普通窗口，有最小化、最大化、关闭按钮。
- Qt.Dialog,对话框窗口，有问号和关闭按钮
- Qt.Popup,弹出窗口，窗口无边框
- Qt.ToolTip,提示窗口，窗口无边框，无任务栏
- Qt.SplashScreen,闪屏，窗口无边框，无任务栏
- Qt.SubWindow,子窗口，窗口无按钮，但有标题。
