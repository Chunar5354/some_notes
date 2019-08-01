PHP7.0语法学习

## 安装

- 在树莓派上
```
sudo apt-get install php php7.0-mysql
```

## 配置

### 显示错误信息

通常.php文件在运行时默认不会在浏览器上显示错误信息，可以通过修改配置文件来显示，方便调试程序

在树莓派上，修改以下文件：
```
--sudo vi /etc/php/7.0/apache2/php.ini 
sudo vi /etc/php/7.0/cli/php.ini
```
改变其中两个参数如下：
```
error_reporting = E_ALL
display_errors = On
```

然后重启，就能够查看错误信息

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
- 19.echo "<pre> ... </pre>";将标签内部的内容排布显示，如表格等
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

- 1.foreach...as 语句对数组进行遍历
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

- 2.使用list...each进行遍历

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

- 3.一些数组的函数
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
