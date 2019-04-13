#git_on_windows

关于在windows上的一些git操作

## 本地Git配置
- 首先在GitHub官网上创建一个账号
- 然后在官网下载git的windows版本：`https://www.git-scm.com/download`
- 在本地创建ssh_key：`$ ssh-keygen -t rsa -C "your_email@youremail.com"`，邮箱就是在GitHub上创建账号的邮箱，之后会创建一个`.ssh`文件夹，里面有一个`id_rsa.pub`文件，复制里面的内容
- 进入GitHub，在`Settings > SSH > ADD SSH`，添加一个SSH，将`id_rsa.pub`中的内容粘贴进去
- 然后输入`ssh -T git@github.com`来验证是否添加成功

## 新建Git仓库

随便在系统中新建一个文件夹，然后进入这个文件夹，输入以下命令：

```python
echo "# test" >> README.md # 为test这个仓库新建 README.md
git init # 初始化当前目录为git仓库
git add README.md #将README.md 添加到仓库
git commit -m "first commit"
git remote add origin https://github.com/Chunar5354/test.git #（改成自己新建的仓库）
git push -u origin master #将改动部署到远程仓库，只有第一次要加‘-u’，把本地 master 分支 推送到 服务器的master分支上，如果服务器没有此分支就新建一个
