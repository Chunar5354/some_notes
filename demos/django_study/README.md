学习一下django框架，看看能不能用它结合mysql搭建一个python的服务器

## 安装

- 树莓派上

```
pip3 install Django
```
安装命令执行之后，会给出一条提醒，说没有将django添加到环境变量中，并会给出当前的django安装位置，可能是`home/pi/.local/bin`

将django添加到环境变量：
```
export PATH=$PATH:/home/pi/.local/bin
```

## 创建项目

可以使用`django-admin`工具来自动创建
```
django-admin startproject mysite
```

会自动在当前目录创建一个`mysite`文件夹，里面包含了初始化的项目文件结构：
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

其中：

- mysite: 项目的容器
- manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互
- mysite/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包
- mysite/settings.py: 该 Django 项目的设置/配置
- mysite/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"
- mysite/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目

这时可以测试一下是否创建成功：
```
python3 manage.py runserver 0.0.0.0:8000    // 后面的地址和端口可以不加，默认是localhost:8000
```

然后在浏览器上输入`localhost:8000`会看到django的默认页面

## 创建app

django的程序运行一般是通过app来实现的，可以在命令行创建app：

```
python manage.py startapp polls     // 创建名为polls的app
```

会新建一个名为polls的文件夹，内部初始结构：
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

还是在浏览器上测试一下，要想能在浏览器山看到自己的内容
