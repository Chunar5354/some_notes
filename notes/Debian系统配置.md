# 用户

## 添加新用户

```
$ adduser username
```

然后按照提示设置密码与信息

## 为用户赋予管理权限

```
$ usermod -aG sudo username
```

可以切换到改用户进行测试：

```
$ su - username
$ sudo whoami
```

## 删除用户

只删除用户，不删除文件

```
$ sudo deluser username
```

删除用户目录

```
$ sudo deluser --remove-home username
```

# 安全

## 禁止root用户远程登陆

编辑`/etc/ssh/sshd_config`文件，将

```
PermitRootLogin yes
```

修改为

```
PermitRootLogin no
```

然=然后重启ssh服务

```
$ sudo service sshd restart
```
