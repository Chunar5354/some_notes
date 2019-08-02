关于在windows上的一些git操作

## 本地Git配置
- 首先在GitHub官网上创建一个账号
- 然后在官网下载git的windows版本：`https://www.git-scm.com/download`
- 设置用户名：`git config --global user.name "name"`
- 设置邮箱：`git config --global user.email "email@xx.com"`
- 在本地创建ssh_key：`ssh-keygen -t rsa -C "your_email@youremail.com"`，邮箱就是在GitHub上创建账号的邮箱，之后会创建一个`.ssh`文件夹，里面有一个`id_rsa.pub`文件，复制里面的内容
- 进入GitHub，在`Settings > SSH > ADD SSH`，添加一个SSH，将`id_rsa.pub`中的内容粘贴进去
- 然后输入`ssh -T git@github.com`来验证是否添加成功

## 新建Git仓库

随便在系统中新建一个文件夹，然后进入这个文件夹，输入以下命令：

```
echo "# test" >> README.md  # 为test这个仓库新建 README.md
git init  #初始化当前目录为git仓库
git add README.md  #将README.md 添加到仓库
git commit -m "first commit"
git remote add origin git@github.com:Chunar5354/newtest.git  #（改成自己新建的仓库），这个是SSH的地址
git push -u origin master  #将改动部署到远程仓库，只有第一次要加‘-u’，把本地 master 分支 推送到 服务器的master分支上，如果服务器没有此分支就新建一个
```

## 本地文件与远程交互

### 上传
在一个初始化好的仓库里面，每次有文件的改动，需要使用以下命令组合将改动上传到远程：
```
git add filename  #改动的那个文件
git commit -m "first commit"  #添加到commit
git push origin master   #push时，如果之前有过其他改动，会出错，需要先将改动pull下来
```

### 下载

```
git pull origin #本地与远程建立了关联时的方式
```
会将github上面的改动都下载到本地

另外有一种方法`clone`，会将指定的仓库下载到当前目录为一个文件夹：
```
git clone git@github.com:Chunar5354/newtest.git #要下载的仓库的SSH地址
```

### remote操作
- 查看remote：`git remote -v`
- 删除remote：`git remote remove <name>`

### 删除文件夹
- `git pull origin master ` # 将远程仓库里面的项目拉下来
- `dir`   # 查看有哪些文件夹
- `git rm -r --cached target`  # 删除target文件夹
- `git commit -m '删除了target'` # 提交,添加操作说明

如果删除时进行了误操作，可以将删除文件恢复:
- `git checkout HEAD filename` 

### 查看状态
- `git status`查看当前仓库状态，是一个很有用的命令，在使用git出错的时候可以使用这个命令查看一些提示

### 出错时一些处理方法
有时git会出现一些异常
- `fatal: loose object`异常：
  - `rm -fr .git`  #将原来的本地git删掉
  - `git init` #重新初始化git来一套
  - `git remote add origin own_url` 
  - `git fetch`
  - `git reset`  
  - `git branch`
  - 这时应该可以继续使用
  
- git pull时报错：`fatal:拒绝合并无关的历史`
  - 在git pull后加上一句：`--allow-unrelated-histories`  #忽略版本不同造成的影响
  
### 重命名文件
- `git mv oldname newname`

## 为github上的.md文件添加目录

- windows系统中：

在[这个网站](https://github.com/ekalinin/github-markdown-toc.go/releases)上下载工具

下载后解压缩，并将要
