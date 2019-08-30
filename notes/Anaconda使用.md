Anaconda是一个Python的科学计算以及机器学习的平台它自带大量Pyhton的科学计算以及机器学习的扩展包，可以很方便的进行相关应用开发

最初是为了要使用cufflinks包，它需要Jupyter Notebook环境，而通过Anaconda来安装Jupyter Notebook非常方便，所以配置了Anaconda

## 安装

在官网下载相应系统的[安装包](https://www.anaconda.com/distribution/#download-section)

### 在windows上

下载一个exe文件，直接执行该文件，按照提示进行安装即可，如果要在命令行使用conda，请将安装的`Anaconda3/Scrpit`路径添加到环境变量中

- 待续

## Jupyter Notebook使用

安装Anaconda通常会同时自动安装Jupyter Notebook，测试一下：
```
jupyter notebook  --version
```

如果没有自动安装的话，可以在Anaconda Prompt中通过下面的命令手动安装：
```
conda install jupyter notebook
```

或者也可以不通过Anaconda，直接使用pip来安装：
```
pip3 install jupyter
```

### 启动Jupyter Notebook

#### 通过Anaconda启动

既然安装了Anaconda，那么也可以通过它来启动jupyter notebook

找到`Anaconda Navigator`这个应用，打开它，会在界面上看到jupyter notebook这个图标，点击它下面的`Lunch`，即可启动


#### 通过命令行启动

直接在命令行输入：
```
jupyter notebook
```

之后打印一系列信息，并在默认浏览器打开一个新的窗口，地址为`http://localhost:8888`（默认地址）

也可以指定窗口启动，如：
```
jupyter notebook --port 9999      // 将会开启9999端口
```

#### 修改默认路径

在jupyter notebook打开的浏览器的界面中，可能会看到一系列文件，其实这个目录就是你计算机本地上的$HOME路径，如果想要为jupyter notebook配置一个新的文件夹，
需要修改配置文件，输入以下命令来获取配置文件的位置：
```
jupyter notebook --generate-config
```

会在下面打印类似这样的信息：
```
Overwrite C:\Users\pp\.jupyter\jupyter_notebook_config.py with default config? [y/N]
```

上面这个是我改动了路径之后，它会提示我是否将配置文件恢复成默认，如果是第一次使用这个命令，只会输出配置文件的位置，
在我这里就是`C:\Users\pp\.jupyter\jupyter_notebook_config.py`，然后打开这个文件，将其中的`c.NotebookApp.notebook_dir`注释去掉，后面加上自定义的文件夹：
```python
c.NotebookApp.notebook_dir = 'your_own_path'    # such as 'C:\User\jupy'
```

然后保存这个文件，再启动jupyter notebook就会发现它已经运行在新目录下了
