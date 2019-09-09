学习一下django框架，看看能不能用它结合mysql搭建一个python的服务器

## 安装

### 树莓派上(Debian)

```
pip3 install Django
```
安装命令执行之后，会给出一条提醒，说没有将django添加到环境变量中，并会给出当前的django安装位置，可能是`home/pi/.local/bin`

将django添加到环境变量：
```
export PATH=$PATH:/home/pi/.local/bin
```

### centos7

```
pip3 install django
```

仍然需要添加环境变量，不过这里要保存在`~/.bash_profile`中，在~/.bash_profile中添加一行：
```
export PATH=$PATH:/usr/local/python3/bin
```

在运行时，可能会因为sqlite的版本过低而出错，即使更新了最新版本也不行，这时，需要在环境变量中添加共享库位置，还是在`~/.bash_profile`中添加一行：
```
 export LD_LIBRARY_PATH="/usr/local/lib"
```

每当修改过该文件之后，执行`source ~/.bash_profile`使改动生效

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

### 在浏览器上显示自定义内容

需要编辑`3个`文件
- 1.首先是`polls/views.py`：
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- 2.然后在polls目录下新建一个`urls.py`文件：
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- 3.最后修改`mysite/urls.py`：
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),   # 文件路径
    path('admin/', admin.site.urls),
]
```

启动django：
```
python manage.py runserver
```

在浏览器中输入`localhost:8000/polls`就能看到views中的内容

- 如果页面显示`DisallowedHost`的错误，需要到`mysite/mysite/settings.py`中改写这一段：
```python
ALLOWED_HOSTS = ['*']   # 在括号中添加'*'
```

## django操作mysql数据库

### 1.配置mysql支持并创建数据库

django默认的数据库是SQLite，要修改成mysql的支持，修改`mysite/settings.py`，将DATABASES配置项的内容替换成下面的内容：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',                           # database name, must be created before
        'USER': 'test',                           # your own mysql user name
        'PASSWORD': 'test123',                    # your password to the user above
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

然后运行：
```
python manage.py migrate
```
就会在`db_name`数据库中创建一系列表（此前确保db_name数据库已经存在，否则会报错）

所创建的表是依据`mysite/settings.py`文件中`INSTALLED_APPS`配置项里面的内容

#### 常见错误

有时执行migrate会提示找不到mysqlclient（比如在centos7系统中），如何在centos7中安装mysqlclient参考[这里](https://github.com/Chunar5354/some_notes/blob/master/notes/Centos%E7%9B%B8%E5%85%B3%E9%85%8D%E7%BD%AE.md)

或者使用`pymysql`来实现migrate，首先安装pymysql：
```
pip3 install pymysql
```

然后修改`mysite/__init__.py`，在其中添加：
```python
import pymysql

pymysql.install_as_MySQLdb() 
```

此时运行`python manage.py migrate`仍然会报错，错误发生在一个`base.py`文件中，编辑它：
```
vim /usr/local/python3/lib/python3.8/site-packages/django/db/backends/mysql/base.py
```

注释掉其中的35 36行

再次运行`python manage.py migrate`仍然会报错，错误发生在一个`operations.py`文件中，编辑它：
```
vim /usr/local/python3/lib/python3.8/site-packages/django/db/backends/mysql/operations.py
```

将其146行的`decode`替换为`encode`

此时可以正常运行`python manage.py migrate`


### 2.为数据库添加自定义数据（models）

- 1.创建新表，编辑`polls/models.py`：
```
from django.db import models

class Question(models.Model):   # 类名对应表名
    # 变量名(question_text)对应列名，后面代表数据类型，CharField相当于mysql中的varchar
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

为了django能够找到polls这个app，还需要进行一项配置：在`mysite/settings.py`文件的`INSTALLED_APPS`配置项中，添加：
```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',  # 这一行是新添加的，代表polls app（polls路径下有一个apps.py文件）
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- 2.然后运行命令：
```
python manage.py makemigrations polls
```

会看到打印出类似下面的信息，表示app包含成功：
```
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
```

- 3.最后，在数据库中创建表格：
```
python manage.py migrate
```

会看到如下信息：
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Rendering model states... DONE
  Applying polls.0001_initial... OK
```
说明表格创建成功，可以到mysql数据库中查看

- tips

在执行完第2步makemigrations之后，会发现在`polls/migrations`目录中多出了一个文件`0001_initial.py`，里面包含了创建表的一些命令，此时可以通过下面的命令查看相应的SQL语句：
```
python manage.py sqlmigrate polls 0001
```

## 创建用户

创建用户之后可以在`localhost:8000/admin`界面登录来查看数据库，输入命令：
```
python manage.py createsuperuser
```

接下来根据提示依次设置用户名、邮箱和密码，新用户创建成功

不过这时在浏览器上登陆看不到我们自己的数据库，还需要将我们的app中数据库的类（在models中）添加到admin注册中，编辑`polls/admin.py`：
```python
from django.contrib import admin
from .models import Question      # 从models文件中引入表

admin.site.register(Question)     # 将表添加到admin中
```

保存该文件，再从浏览器上登录，就能够看见`Question`表，并对其进行操作

## 添加已有的数据库

首先修改`mysite/settings.py`中的DATABASES：
```python
DATABASES = {
    'default': {
        'NAME':'jd',            # 改成要添加的数据库名
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'yourpasswd',
    }
}
```

然后在命令行中：
```
python manage.py inspectdb > ./polls/models.py
```

就会在polls文件夹中生成新的models.py替换原来的文件

再执行：
```
python manage.py migrate
```
就将新的数据库添加到了django的配置当中

- tips：注意要再`mysite/setings.py`中的 `INSTALLED_APPS` 配置项中包含models的app（因为有可能不是polls）
