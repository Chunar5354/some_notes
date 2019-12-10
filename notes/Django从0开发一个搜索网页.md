## 简介

这个项目是跟随Youtube上的一个视频学习的，[视频链接](https://www.youtube.com/watch?v=JT80XhYJdBw)

原项目的[Github地址](https://github.com/CleverProgrammer/codedaddies_list)

### 用到的一些资源

- [Materialize](https://materializecss.com/)一个超级好用的免费html模板网站

- [CodePen](https://codepen.io/)网页前端测试平台，本身也做的很美观

## 开发过程

### django安装

如果是在anaconda虚拟环境的话:
```
# conda install django
```

其他的安装[参考这里](https://github.com/Chunar5354/some_notes/tree/master/demos/django_study#%E5%AE%89%E8%A3%85)

### 创建项目框架

- 1.创建项目文件夹
```
# django-admin startproject studyapp
```

- 2.创建app
```
# python manage.py startapp myapp
```

- 3.创建模板文件夹

在根目录下
```
# mkdir templates
```
并在其中新建一个`base.html`文件
```
# vim templates/base.html
```
这个就是我们html文件的存放路径

然后注意要将templates文件夹添加到django的设置中，编辑`stuayapp/settings.py`文件，在其中添加一行
```python
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```
并将`TEMPLATE_DIR`添加到`TEMLATES`中：
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],    # 添加到这里
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 4.创建css样式文件夹

在根目录下新建一个`static`文件夹
```
# mkdir static
```
然后在其中新建一个`css/style.css`文件（这个文件可以根据自己的喜好）

然后也是要把static添加到django的设置中，编辑`studuapp/settings.py`文件，在其中新建一行
```python
STATIC_URL = '/static/'   # 这一行可能本来就有
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
```

### 程序编写

具体的程序可以参考源码，这里主要说明一下编写的思路

- 1.弄一个html文件，比如`templates/base.html`

- 2.把html文件添加到`myapp/views.py`中（myapp就是自定义的app名称）
```python
# myapp/views.py
from django.shortcuts import render

def home(request):
  # 使用render方法可以将html文件渲染
  # 注意这里的base.html一定要是在templates文件夹下，而且tamplates要添加到settings中
	return render(request, 'base.html')
```

- 3.把`myapp/views.py`添加到`myapp/urls.py`中
```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),    # home是views.py中定义的函数
]
```

- 4.把`myapp/urls.py`添加到`studyapp/urls.py`中（studyapp是那个包含了settings.py的文件夹）
```python
# studyapp/urls.py
from django.contrib import admin
from django.urls import path, include

# The first argument in path() is how you search the url in your browser
urlpatterns = [
	  path('', include('myapp.urls')),   # 这一句是自己添加的，其中path的第一个参数是你要在浏览器中搜索的路径
    path('admin/', admin.site.urls),
]
```

以上步骤都完成之后就可以在浏览器中搜索`ip:port`（因为path的第一个参数是空字符串）来查看base.html中的内容了

### 关于数据库

与数据库有关的程序要写在`myapp/models.py`中，例如：
```python
from django.db import models

# Create your models here.
# 在mysql数据库中，表名是myapp_search(app名称+class名称）
# search和created都是列名
class Search(models.Model):
	search = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		# This can show the name of search if admin page, not just 'Search object'
		return '{}'.format(self.search)

	class Meta():
		# This can change the displayed 'Searchs' into 'Searches'
		# Because django automaticlly add a 's' at the end of class-name
		verbose_name_plural = 'Searches'
```

#### 数据库中数据的使用

比如在本例中，`myapp/views.py`中有这样一段代码；
```python
search = request.POST.get('search')
# 把上面通过POST请求获取的数据添加到数据库中（因为created被设置成了自动添加，所以这里只需要传入一个search参数）
models.Search.objects.create(search=search)
```

### html前端和python后端的联动

在上一小节中我们看到`myapp/views.py`中有这样一段代码
```python
search = request.POST.get('search')
```

它就是表示从html前端获取数据，它能实现因为在`base.html`中有这样一段代码:
```html
<!-- use form to create a input line -->
  <!-- 注意这里的 {% url 'new_search' %} ，它表示当点击按钮或者回车之后会跳转到'ip:port/new_search'页面，要提前把它添加到views和urls中 -->
  <!-- 这里的 method="post" 和views.py中的 POST 对应 -->
	<form action="{% url 'new_search' %}" method="post">
		<!-- add csrf_token here, or when you type 'Enter' or click the button, there will be an error -->
		{% csrf_token %}
		<!-- placeholder is the default value when you have not type any words in -->
    <!-- 这里的 name="search" 所以在views.py中是 get('search') -->
		<input type="text" name="search" placeholder="search">
		<button class="btn waves-effect waves-light" type="submit" name="action">Submit
			<i class="material-icons left">search</i>
		</button>
		<!-- type 'text' is a input line, type 'submit' is a button -->
	</form>
```

所以views.py中获取的是输入行<input>中的内容，随后跳转到new_search页面

### html的一些知识

#### 用到的语法知识

- 1.普通标签用`<>`
  - 要为某一元素添加链接要使用`<a>`标签将其包装
  
- 2.引用变量用`{{}}`

- 3.写逻辑代码用`{% %}`

- 4.`{% for %}` 循环中列表下标使用`.`来表示，如`{{ book.0 }}`

#### 代码扩展

使用下面的
```html
{% block content %}

{% endblock content %}
```
在当前文件（如base.html）中留出一块区域，用来添加`其他html文件`中的代码

而其他文件可以在复制上面的base.html文件中所有代码的情况下，添加新的代码
```html
<!-- 复制base.html中的内容 -->
{% extends 'base.html' %}

<!-- 添加新代码到block中 -->
{% block content %}
<!-- 新代码 -->
{% endblock content %}
```

这样就能在新文件中保留base.html内容的同时增加自定义的新代码


#### 在头部引入外部css

```html
{% load static %}
<!-- 下面第一行引用的是本地文件，static要在头部通过loas引入，注意static要添加到settings中 -->
<link rel="stylesheet" href="{% static "css/style.css" %}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```


## 总结

其实大框架django都已经设计好了，用户只需要往指定的文件中写入内容就可以了，有几点需要注意：

- 1.各个urls的路径设置问题
- 2.models文件中操作数据库的问题
- 3.其实主要的后端逻辑是在views.py中完成的（因为要把views.py中的函数添加到urls中）
