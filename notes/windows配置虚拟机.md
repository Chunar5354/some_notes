通过[Vargant](https://www.vagrantup.com/downloads.html)和[VirtualBox](https://www.virtualbox.org/wiki/Downloads)这两个工具来实现

参考了[这篇文章](https://github.com/marogatari/marogatari.github.io/blob/master/CodeExperience/vagrant/init_vagrant.md)

- 首先要下载安装这两个工具，根据官方提示即可

## 配置VirtualBox

- 1.需要手动下载一个[虚拟机文件](https://app.vagrantup.com/boxes/search)，自行选择需要的操作系统下载
- 2.新建一个文件夹来放置box配置文件和虚拟机文件，文件结构如下：
```
>vbox
  >box_file // 将下载的虚拟机文件放在这里
  >conf_file // 这里放置配置文件
```
- 3.在上面的`conf_file`文件夹中打开命令行，输入命令：
```
vagrant box add BOXNAME BOXPATH
```
其中`BOXNAME`是为虚拟机容器起的名字，`BOXPATH`是下载的虚拟机文件路径

之后会输出以下信息：
```
C:\Codes\Vagrant\Amadeus>vagrant box add Amadeus ..\VM\CentOS-7-x86_64-Vagrant-1905_01.VirtualBox.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'Amadeus' (v0) for provider:
    box: Unpacking necessary files from: file://C:/Codes/Vagrant/VM/CentOS-7-x86_64-Vagrant-1905_01.VirtualBox.box
    box: Progress: 100% (Rate: 244M/s, Estimated time remaining: --:--:--)
==> box: Successfully added box 'Amadeus' (v0) for 'virtualbox'!
```

然后输入命令`vagrant init`，输出以下信息：
```
C:\Codes\Vagrant\Amadeus>vagrant init
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
```

## 配置Vargant

按照上面的操作进行成功的话在`conf_file`文件夹中会出现一个`Vagrantfile`文件，它是虚拟机的配置文件，使用Ruby语言所编写，通过编写文件中的内容来配置虚拟机

### 命名

在`Vagrantfile`添加以下内容：
```
config.vm.box = "BOXNAME"       // 这里的BOXNAME和上面的BOXNAME要一样
config.vm.hostname = "name"     // name为自定义用户名
config.vm.define "vbox"         // 虚拟机名称
```

然后在`config.vm.provider "virtualbox" do |vb|`这一行之后添加：
```
vb.gui = false     // 不要图形界面
vb.name = "vbox"   // 文件目录名称
```

### 网络设置

在`Vagrant.configure("2") do |config|`这一段中（应该会有和下面内容类似的行，就放在它后面）添加以下内容，配置IP地址以及端口：

```
config.vm.network "forwarded_port", guest: 80, host: 8080     // guest表示虚拟机，host表示windows
config.vm.network "private_network", ip: "192.168.22.22"      // 虚拟机的ip地址，可以任意设置
```

### 文件共享

在上一节内容的下面添加以下内容，设置虚拟机与主机的共享文件夹:

```
config.vm.synced_folder "C:/Codes/Projects", "/home/projects"
```
前面是主机上的文件夹，后面是虚拟机上的文件夹，相应地改成自己的文件

## 多个虚拟机配置
大体与上面的配置方法相似，但是要针对每个虚拟机分别配置，如下所示：
```ruby
Vagrant.configure("2") do |config|
  config.vm.define "cbox" do |cbox|
    config.vm.box = "centbox"
    config.vm.hostname = "Chunar"
    config.vm.network "private_network", ip: "192.168.11.11"
    config.vm.synced_folder "P:/share/share_c", "/home/vagrant/share"
  end

  config.vm.define "ubox" do |ubox|
    config.vm.box = "ubunbox"
    config.vm.hostname = "Qiuer"
    config.vm.network "private_network", ip: "192.168.11.22"
    config.vm.synced_folder "P:/share/share_q", "/home/vagrant/share"
  end
  config.vm.network "forwarded_port", guest: 80, host: 8080
end
```

## 开机

首先需要安装一个`vbguest`插件，在命令行输入下面命令：
```
vagrant plugin install vagrant-vbguest
```

等待一段时间，输出下面的信息：
```
Installing the 'vagrant-vbguest' plugin. This can take a few minutes...
Fetching: micromachine-2.0.0.gem (100%)
Fetching: vagrant-vbguest-0.18.0.gem (100%)
Installed the plugin 'vagrant-vbguest (0.18.0)'!
```

这样说明安装成功，可以输入`vargant up`命令开机，首次开机需要配置内核，可能会花费比较长的时间

- 一些控制命令（在windows命令行下）：
```
vargant up               // 开机
vagrant reload           // 重载
vargant ssh              // 登陆到虚拟机的命令行
vargant halt             // 关机
vagrant status           // 查看状态
vagrant box list         // 查看当前所有虚拟机
vagrant box remove ..    // 删除某虚拟机
注意执行这些命令也要在conf_file文件夹中进行
```
