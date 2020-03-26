PHP7.0语法学习

* [安装](#%E5%AE%89%E8%A3%85)
* [配置](#%E9%85%8D%E7%BD%AE)
  * [显示错误信息](#%E6%98%BE%E7%A4%BA%E9%94%99%E8%AF%AF%E4%BF%A1%E6%81%AF)
* [知识点](#%E7%9F%A5%E8%AF%86%E7%82%B9)
  * [基础](#%E5%9F%BA%E7%A1%80)
  * [关于类](#%E5%85%B3%E4%BA%8E%E7%B1%BB)
  * [关于数组](#%E5%85%B3%E4%BA%8E%E6%95%B0%E7%BB%84)
    * [1\.foreach\.\.\.as 语句对数组进行遍历](#1foreachas-%E8%AF%AD%E5%8F%A5%E5%AF%B9%E6%95%B0%E7%BB%84%E8%BF%9B%E8%A1%8C%E9%81%8D%E5%8E%86)
    * [2\.使用list\.\.\.each进行遍历](#2%E4%BD%BF%E7%94%A8listeach%E8%BF%9B%E8%A1%8C%E9%81%8D%E5%8E%86)
    * [3\.一些数组的函数](#3%E4%B8%80%E4%BA%9B%E6%95%B0%E7%BB%84%E7%9A%84%E5%87%BD%E6%95%B0)
  * [文件处理](#%E6%96%87%E4%BB%B6%E5%A4%84%E7%90%86)
    * [1\.检测文件是否存在](#1%E6%A3%80%E6%B5%8B%E6%96%87%E4%BB%B6%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8)
    * [2\.文件读写](#2%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99)
    * [3\.复制文件](#3%E5%A4%8D%E5%88%B6%E6%96%87%E4%BB%B6)
    * [4\.为文件加锁](#4%E4%B8%BA%E6%96%87%E4%BB%B6%E5%8A%A0%E9%94%81)
    * [5\.读取整个文件](#5%E8%AF%BB%E5%8F%96%E6%95%B4%E4%B8%AA%E6%96%87%E4%BB%B6)
    * [6\.上传文件](#6%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)
  * [系统调用](#%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8)
* [PHP操作MYSQL数据库](#php%E6%93%8D%E4%BD%9Cmysql%E6%95%B0%E6%8D%AE%E5%BA%93)
  * [创建登陆文件](#%E5%88%9B%E5%BB%BA%E7%99%BB%E9%99%86%E6%96%87%E4%BB%B6)
  * [获取数据库中的内容](#%E8%8E%B7%E5%8F%96%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%AD%E7%9A%84%E5%86%85%E5%AE%B9)
  * [在页面中与数据库交互](#%E5%9C%A8%E9%A1%B5%E9%9D%A2%E4%B8%AD%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BA%A4%E4%BA%92)
    * [关于\_POST数组](#%E5%85%B3%E4%BA%8E_post%E6%95%B0%E7%BB%84)
    * [全部程序](#%E5%85%A8%E9%83%A8%E7%A8%8B%E5%BA%8F)


## 安装

以下安装均针对PHP7.3版本

- 在Debian系统上
```
# sudo apt-get install php7.0 php7.3-mysql
```

- 在Centos系统上

首先可以安装一个`Remi`源，通过它来安装php
```
# sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

配置启用Remi源
```
# sudo yum-config-manager --enable remi-php73
```

安装php
```
# sudo yum install php73-php -y
```

安装依赖管理器`composer`
```
# sudo yum install composer -y
```

## 配置

### 配置nginx运行php文件

nging需要通过`php-fpm`来运行php文件，安装:
```
# yum install php-fpm php-pdo php-mysql php-xml
```

启动php-fpm：
```
# systemctl start php-fpm
```

修改nginx的配置文件

```
# vim /etc/nginx/nginx.conf
```

添加以下内容:
```conf
	location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }

        # 这里是新增内容
        # PHP 脚本请求全部转发到 FastCGI处理. 使用FastCGI协议默认配置.
        # Fastcgi服务器和程序(PHP,Python)沟通的协议.
        location ~ \.php$ {
            # 设置php文件存放路径, php-fpm默认的路径是/var/www/html, 与nginx不同
			root /var/www/html;
			# 设置监听端口，php-fpm默认端口是9000
            fastcgi_pass   127.0.0.1:9000;
            # 设置nginx的默认首页文件(可以没有)
            fastcgi_index  index.php;
            # 设置脚本文件请求的路径
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            # 引入fastcgi的配置文件
            include        fastcgi_params;
        }
```

然后重启nginx:

```
systemctl restart nginx
```

然后将php文件放到`/var/www/html`路径中就可以通过http请求来运行

### 显示错误信息

通常.php文件在运行时默认不会在浏览器上显示错误信息，可以通过修改配置文件来显示，方便调试程序

在树莓派上，修改以下文件：
```
# sudo vi /etc/php/7.0/apache2/php.ini 
# sudo vi /etc/php/7.0/cli/php.ini
```
改变其中两个参数如下：
```
error_reporting = E_ALL
display_errors = On
```

然后重启，就能够查看错误信息

但是这样不太安全，再进行实际应用的时候要修改回来

## 知识点

### 基础

- 1.php代码要放在标记内部 
```
<?php
...
?>
```
- 2.php中的注释为`//`，多行注释使用`/* ... */`
- 3.php每一行末尾都要加上`;`
- 4.php中声明变量用`$`符号，并且在`双引号`字符串中的`$`也会被当作变量声明
- 5.转义字符只在`双引号`字符串中起作用，`单引号`字符串中转义字符只有 `\'`和 `\\`
- 6.多行文本可以使用`双引号`，或者`<<< _END  ...   _END`结构（后面的_END必须单独放一行）
- 7.字符串转为数字不需要任何操作，直接计算即可
- 8.使用define（常量名， 内容）函数可以定义常量 （类似C语言宏定义）
- 9.函数声明使用`function funcname(){}`
- 10.在函数中定义静态变量，运行后其值会保留：`static $x`
- 11.使用`htmlentities()`进行清洁处理，增强安全性
- 12.php中FALSE值为NULL，TRUE值为1
- 13.php中一致性运算符`===`用来取消强制的类型转换，或者`!== `
- 14.在行尾加上`"<br>"`标签可以强制另起一行输出
- 15.类型转换需要加括号 如 `(int)(1.1);`
- 16.即使在函数返回值中返回多个参数的元组，也要加上array：`return array($a1, $a2, $a3); `
- 17.使用`print_r`来打印变量、数组或者对象中的内容
- 18.关联数组`$array['a']='b'`，类似字典
- 19.`echo "<pre> ... </pre>";`将标签内部的内容排布显示，如表格等
- 20.`printf()`可以加`%`将字符串进行格式化显示，也可以使用`sprintf()`将格式化字符串作为参数传递
- 21.`time()`返回当前UNIX时间戳，也可以使用`mktime()`为任意时间（1970--2038）创建时间戳
- 22.使用`date($format, $timestamp)`函数显示日期，$format是一个格式化字符串，有标准定义的字符来代表各个意义；$timestamp为时间戳

### 关于类

- 1.使用class创建类，使用new ...创建实例
- 2.调用类中的属性和函数使用 `->`如class->function()
- 3.使用`clone`操作符克隆对象，使得修改后面的对象不会对前面的对象产生影响：$object2 = clone $object1;
- 4.类中的this（等同于python的self） 调用属性使用`this->xx`，调用方法使用`self::xx()`
- 5.在类中也可以使用静态方法`static`它不能访问任何对象属性，通常用于调用类本身，而且调用的方法不是->而是`::`而且静态的属性和方法不必实例化就可访问
- 6.在类中声明常量使用`const`语句，并使用self::the_const 来引用常量
- 7.三种属性和方法的作用范围`public`（外部可调用），`protected`（外部不可调用，派生类可调用），`private`（外部不可调用，派生类也不可调用，只有自身可调用）
- 8.类继承，使用`extends` ：class ChildClass extends FatherClass
- 9.类中的初始化：`__construct()`(类似__init__)

### 关于数组

#### 1.foreach...as 语句对数组进行遍历
```php
<?php
$paper = array("Cpoier", "Inkjet", "Laser", "Photo");
$j = 0;

foreach ($paper as $item)  // 将&paper数组中的元素作为变量$item进行遍历
{
  echo "$j: $item<br>";
  ++$j;
}
?>
```

也可以对关联数组进行遍历
```php
<?php
$paper = array("Cpoier" => "C123",
               "Inkjet" => "I456",
               "Laser"  => "L789",
               "Photo"  => "P321");

foreach ($paper as $item => $description)  // 将&paper数组中的键作为变量$item，值作为$description进行遍历
{
  echo "$item: $description";
}
?>
```

#### 2.使用list...each进行遍历

与foreach ...as方法的功能类似
```php
<?php
$paper = array("Cpoier" => "C123",
               "Inkjet" => "I456",
               "Laser"  => "L789",
               "Photo"  => "P321");

while (list($item, $description) = each($paper))  // 将&paper数组中的键作为变量$item，值作为$description进行遍历
// 注意与foreah ...as的区别
{
  echo "$item: $description";
}
?>
```

#### 3.一些数组的函数
```php
// 1. is_array
// 判断变量是否为一个数组
echo (is_array($the_array)) ? "Is an array" : "Is not an array";

// 2. count
// 返回数组中的元素个数

// 3. sort 
// 排序
sort($fred, SORT_NUMERIC)  // 指定按照数值排序
sort($fred, SORT_STRING)   // 指定按照字符串排序
rsort($fred, SORT_NUMERIC)  // 指定按照数值，相反顺序排序
rsort($fred, SORT_STRING)   // 指定按照字符串，相反顺序排序

// 4. shuffle
// 将数组中的元素随机顺序排序

// 5. explode
// 将字符串分割成数组，类似Python中的split
<?php
$temp = explore(' ', "This is a sentence with seven words");
print_r($temp);
?>

// 6. extract
// 将关联数组中的元素提取出来作为变量，键为变量名，值为变量的值
<?php
$paper = array("Copier" => "C123",
               "Inkjet" => "I456",
               "Laser"  => "L789",
               "Photo"  => "P321");

extract($paper);
// 然后便可以调用$Copier等变量
echo $Copier . $Inkjet . $Laser . $Photo;
{
  echo "$item: $description";
}
?>
// 有时提取的变量与原有的变量产生冲突，使用下面方法
extract($paper, EXTR_PREFIX_ALL, 'format');
// 则所有的变量名前都加上了format_前缀，变成了$format_Copier

// 7. compact
// 与extract相反，通过变量来创建数组
<?php
$a = "aaa";
$b = "bbb";
$c = "ccc";

$contact = compact('a', 'b', 'c');
print_r($contact);
?>
```

### 文件处理

#### 1.检测文件是否存在

使用file_exists函数
```php
if ((file_exists("testfilt.txt")) echo "File exists";
```

#### 2.文件读写

首先使用fopen函数来打开一个文件
```php
<?php
$fh = fopen("testfile.txt", 'w') or die("Failed to open file");
?>
```

其中第一个参数为文件名，第二个参数表示文件的打开模式，共有六种:

| 模式  |              行 为               |
| ---- | ------------------------------- |
| 'r'  | 从文件头部开始读                   |
| 'r+' | 从文件头部开始，可读写            |
| 'w'  | 从文件头部开始写，删除原内容        |
| 'w+' | 从文件头部开始，可读写，删除原内容  |
| 'a'  | 从文件尾部开始追加内容              |
| 'a+' | 从文件尾部开始追加内容，可读写      |

将数据写入文件使用`fwrite()`函数

读取文件内容使用`fgets()`函数（读取一行），或者`fread($fh, num)`（读取num个字符长度的内容）

#### 3.复制文件

使用copy函数复制文件
```php
<?php
if (!copy('testfile.txt', 'testfile2.txt')) echo "Could not copy file";
else echo "File successfully copied to 'testfile2.txt'.";
?>
```

相似的，可以使用`rename(old_name, new_name)`对文件重命名

以及`unlink(filename)`删除文件

#### 4.为文件加锁

在多用户访问的时候，为防止产生冲突，需要对文件加锁，使用`flock()`函数

```php
<?php
$fh = fopen("testfile.txtx", 'r+') or die("Failed to open file);
$text = fgets($fh);

if (flock($fh, LOCK_ex))  // 为文件上锁
{
  fseek($fh, 0, SEEK_END);  //将指针定位到文件末尾
  fwrite($fh, "$text") or die("Cound not write to file");
  flock($fh, LOCK_UN);    //操作完毕，将文件解锁
}

fclose($fh);  // 在程序末尾关闭连接
?>
```

#### 5.读取整个文件

使用`file_get_contents`函数可以获取整个文件的内容，还有另一个很好用的功能是可以读取一个`HTML页面`

```php
<?php
echo file_get_contents("http://oreilly.com");
?>
```

#### 6.上传文件

主要使用到`$_FILES`数组，还有一个demo在书上`P146 例7-15`，在树莓派上尝试的时候失败了

### 系统调用

使用`exec()`函数来进行系统调用，可以将一些命令行操作的结果打印出来，但是似乎没有真正的进行相关操作（比如重启就不行）

```php
<?php
$cmd = 'ls';
exec(escapeshellcmd($cmd), $output, $status);

if ($status) echo "Exec command failed";
else
{
  echo "<pre>";
  foreach($output as $line) echo htmlspecialchars("line\n");
  echo "</pre>";
}
?>
```

## PHP操作MYSQL数据库

### 创建登陆文件

为了使用PHP登录mysql数据库，首先创建一个登陆文件，里面包含数据库的信息：

```php
<?php  // login.php
$db_hostname = 'localhost';
$db_database = 'database_name';
$db_username = 'user_name';
$db_password = 'password';
?>
```

将其中的用户名和密码等信息替换成1自己的信息，保存成一个`login.php`文件

### 获取数据库中的内容

- 首先使用`mysqli()`函数建立连接，新建对象$conn
- 使用$conn对象中的`query`方法，来执行SQL语句，返回一个$result对象
- 使用$result中的`data_seek(num)`方法来定位指针到数据库的指定行
- 然后使用$result中的`fetch_array()`方法将改行内容保存为一个数组，根据括号中传入的参数不同，数组的形式也不同。`MYSQLI_ASSOC`对应关联数组；`MYSQLI_NUM`对应数值数组；`MYSQLI_BOTH`为二者结合
- 最后要将$result和$conn关闭（$close())

```php
<?php
require_once 'login.php';
$conn = new mysqli($db_hostname, $db_username, $db_password, $db_database);
// users can use the objects in module directly
if ($conn->connect_error) die($conn->connect_error);
$query = "SELECT * FROM pet";
$result = $conn->query($query); // pay attention to this function 'query'
if (!$result) die($conn->error);
$rows = $result->num_rows; // return the number of rows in $result
echo "<pre>";
for ($j=0; $j<$rows; ++$j)
{
		$result->data_seek($j);
		$row = $result->fetch_array(MYSQLI_ASSOC);
		// return all data in one row as the type 'array'
		echo 'Name:' . $row['name'] . '<br>';
		echo 'Owner:' . $row['owner'] . '<br>';
		echo 'Sex:' . $row['sex'] . '<br>';
		echo 'Birth:' . $row['birth'] . '<br>';
		echo 'Death:' . $row['death'] . '<br><br>';
}
/*
for ($j=0; $j<$rows; ++$j)
		echo 'Name:' . $rows['name'] / '<br>';
		$result->data_seek($j);
		echo 'Name:' . $result->fetch_assoc()['name'] . '<br>';
		// return all data in one row as the type 'array'
		$result->data_seek($j);
		echo 'Owner:' . $result->fetch_assoc()['owner'] . '<br>';
		$result->data_seek($j);
		echo 'Birth:' . $result->fetch_assoc()['birth'] . '<br>';
		$result->data_seek($j);
		echo 'Sex:' . $result->fetch_assoc()['sex'] . '<br>';
		$result->data_seek($j);
		echo 'Death:' . $result->fetch_assoc()['death'] . '<br><br>';
}
// pay attention to the function 'data_seek' and 'fetch_assoc'
// */
$result->data_seek(2);
print_r($result->fetch_array(MYSQLI_BOTH));
echo "</pre>";
$result->close();
$conn->close();
?>
```

### 在页面中与数据库交互

#### 关于_POST数组
使用`$_POST`关联数组来捕捉页面上的用户输入信息，定义一个函数：

```php
function get_post($conn, $var)
{
		print_r($_POST);
		return $conn->real_escape_string($_POST[$var]);
}
```
其中`$conn`为创建的连接对象，`$var`为`$_POST`数组中的键（对应form表单中name字段的值）

使用`real_escape_string`的目的是将字符串强制转义，防止其中的特殊字符引起错误

#### 全部程序

```php
<?php
require_once 'login.php';
$conn = new mysqli($db_hostname, $db_username, $db_password, $db_database);
if ($conn->connect_error) die($conn->connect_error);
if (isset($_POST['delete']) && isset($_POST['birth']))
{
		$birth = get_post($conn, 'birth');
		$query = "DELETE FROM pet WHERE birth='$birth'";
		$result = $conn->query($query);
		if (!$result) echo "DELETE failed: $query<br>" . $conn->error . "<br><br>";
}
if (isset($_POST['name']) &&
	isset($_POST['owner']) &&
	isset($_POST['species']) &&
	isset($_POST['sex']) &&
	isset($_POST['birth']) &&
	isset($_POST['death']))
{
		$name = get_post($conn, 'name');
		$owner = get_post($conn, 'owner');
		$species = get_post($conn, 'species');
		$sex = get_post($conn, 'sex');
		$birth = get_post($conn, 'birth');
		$death = get_post($conn, 'death');
		$query = "INSERT INTO pet VALUES" . 
				"('$name', '$owner', '$species', '$sex', '$birth', '$death')";
		$result = $conn->query($query);
		if (!$result) echo "INSERT dailed: $query<br>" . 
				$conn->error . "<br><br>";
}
echo <<<_END
<form action="sqltest.php" method="post"><pre>
Name <input type="text" name="name">
Owner <input type="text" name="owner">
Species <input type="text" name="species">
Sex <input type="text" name="sex">
Birth <input type="text" name="birth">
Death <input type="text" name="death">
<input type="submit" value="ADD RECORD">
</pre></form>
_END;
$query = "SELECT * FROM pet";
$result = $conn->query($query);
if (!$result) die("Database access failed:" . $conn->error);
$rows = $result->num_rows;
for ($j=0; $j<$rows; ++$j)
{
		$result->data_seek($j);
		$row = $result->fetch_array(MYSQLI_NUM);
		echo <<<_END
		<pre>
		Name $row[0]
		Owner $row[1]
		Species $row[2]
		Sex $row[3]
		Birth $row[4]
		Death $row[5]
		</pre>
		<form action="sqltest.php" method="post">
		<input type="hidden" name="delete" value="yes">
		<input type="hidden" name="birth" value="$row[4]">
		<input type="submit" value="DELETE RECORD">
		</form>
_END;
}
$result->close();
$conn->close();
function get_post($conn, $var)
{
		print_r($_POST);
		return $conn->real_escape_string($_POST[$var]);
}
?>
```

- 该程序的逻辑为：

首先使用`isset`检查delete按钮是否按下以及`'birth'`字段否有值（由于birth没有重复，将其设为主键），若检测成功，则执行相应的删除操作；

然后检测如果全部输入框都有内容输入，则执行一次插入命令，输入框通过form表单的形式构造，以echo 字符串形式显示（注意form表单中name字段的值与_POST数组的对应关系；

最后将表中所有行逐一查询显示，并附带可操作的删除按钮。

- 以上全部功能都可以通过mysqli的另一套规范化函数实现，具体内容查看书上`P240`

## workerman

workerman是一个php的服务器框架，使用它可以方便地处理各种协议，进行数据传输

### 安装

首先查看是否已经安装了workerman所需要的依赖：
```
# curl -Ss http://www.workerman.net/check.php | php
```

如果输出的每一行后面都有`[ok]`字样，说明已经安装了全部依赖（树莓派上似乎按照上面的方法安装php就已经同时完成了依赖的安装）

安装workerman（其实是一个代码包，从github上下载）：
```
# git clone https://github.com/walkor/workerman
```

### 测试

创建一个`test_worker.php`文件：
```php
<?php
use Workerman\Worker;
require_once './Workerman/Autoloader.php';

// 创建一个Worker监听2347端口，不使用任何应用层协议
$tcp_worker = new Worker("tcp://0.0.0.0:2347");

// 启动4个进程对外提供服务
$tcp_worker->count = 4;

// 当客户端发来数据时
$tcp_worker->onMessage = function($connection, $data)
{
    // 向客户端发送hello $data
    $connection->send('hello ' . $data);
    echo "success";
};

// 运行worker
Worker::runAll();
```

然后在命令行输入命令：
```
# php test_worker.php start
```

此时workerman会以调试模式运行，打开浏览器，输入`localhost:2347`，每次刷新页面都会在命令行输出一个"success"

或者使用`telnet`输入地址和端口进行测试，输入任意字符串如'test'，会输出结果'hello test'

### 常用命令

workerman有以下命令：
```
php test.php start          // 以调试模式运行
php test.php start -d       // 在后台运行，会推出到命令行，需要通过stop关闭
php test.php stop           // 关闭
php test.php status         // 查看状态
```
