关于ssh远程连接，以及传输文件

## 远程连接

使用ssh命令

```
ssh username@servername
```

其中`username`和`servername`分别是远程设备的用户名和ip地址，之后需要输入密码进行连接

## 上传/下载文件

### 下载文件到本地

使用scp命令：
```
scp username@servername:/path/filename /var/www/local_dir
```

其中：

- `username`和`servername`分别是远程设备的用户名和ip地址
- 前面的路径为远程设备上目标文件的路径，后面的路径为本地的保存路径
- 如果是传输文件夹则要加上`-r`参数

### 上传文件到远程设备

使用scp命令：
```
scp /path/filename username@servername:/path
```

其中：

- `username`和`servername`分别是远程设备的用户名和ip地址
- 前面的路径为本地文件的路径，后面的路径为远程设备保存的路径
- 如果是传输文件夹则要加上`-r`参数

### 指定端口

所有的以上ssh命令都可以使用`-P`参数来指定端口，如：
```
scp -P 8000 /path/filename username@servername:/path             // 指定8000端口
```
