有时需要一个程序在后台不间断地运行，在linux系统上，一般有两种办法

## 1.nohup

## 2.service

顾名思义，就是将自己的python脚本添加到系统服务中，以centos7系统为例，在`/lib/systemd/system/`目录下添加一个新的service文件：
```
sudo vim /lib/systemd/system/myapp.service
```

在其中输入以下内容：
```
[Unit]
Description=My Service
After=multi-user.target
 
[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/myapp.py
 
[Install]
WantedBy=multi-user.target
```

其中：
- `Description`是对这个服务的描述
- `After`表示这个服务会在multi-user环境启动之后运行
- `Type`为idle确保脚本在其他东西加载完成之后运行
- `ExecStart`的前半段为这个脚本的启动引擎，后半段为该脚本的绝对路径

写好service文件后，需要重启service使配置生效：
```
sudo systemctl daemon-reload
sudo systemctl start myapp.service
```

服务启动成功，可以输入下面的命令来查看该服务的运行状态：
```
service myapp status
```

重定向输出信息（待修改）：
```
ExecStart=/usr/bin/python /home/snail/autorun.py > /home/snail/autorun.log 2>&1
```
