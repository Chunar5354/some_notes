《Python学习手册》的学习记录

## 随时记录的知识点

- 1.使用`set()`函数可以从一个序列创建集合
- 2.使用`decimal`模块创建小数对象，比浮点数运算精确     书-P167
- 3.切片`s[1:9:2]` 2表示步长，就是隔一个取一个，`s[1:9:-1]` 负数表示从右往左取
- 4.一个概念：方法总与对象相关联，方法调用表达式 object.method(arguments) 表示 使用参数调用方法来处理对象
- 5.使用列表的切片也可以实现`插入`操作： `l[1:1] = [2, 3]，l[:0] = [2, 3]`（在头部插入），`[len(l):] = [2, 3]`，在末尾插入
- 6.字典中有一个`d.get(key, default)`方法，获取对应键的值，如果键不存在，则返回后面default设置的值
- 7.使用`sys.stdout()`可以将print打印的内容保存到文件
- 8.`enumerate()`函数返回序列某个元素的偏移量和值，返回一个迭代器对象
- 9.`os.system()`可以运行一个命令行命令
- 10.`python -m pydoc -b` 会将当前目录下的py文件以及python内置库文件显示在HTML页面中，可以查看他们的文档
- 11.`x.copy()`复制可变对象，对于列表，可以使用切片`l2=l1[:] `(列表没有copy方法）
- 12.使用 `del name` 语句可以删除定义的变量名

### 通过'#!'创建脚本文件

通常在命令行运行一个.py文件需要输入如`python test.py`的命令

但是如果将其设置为脚本文件就可以通过在命令行输入文件名直接运行，做法为在文件的最上面插入一行：
```
#! /usr/bin/python
```
后面的内容是python的安装路径，在我的树莓派上路径为`/usr/bin/python`

然后可以在命令行输入`./test.py`来运行这个脚本文件

### 查看帮助

可以对任意一个对象使用`dir(x)`来查看这个对象可调用的方法，以及使用`help(x)`查看详细信息

### '__'双下划线创建内置函数

> 一般来说，以双下划线开头并结尾的变量名用来表示Python实现细节的命名模式。而没有下划线的属性是其他对象能够调用的方法。

在自定义类的时候，可以创建一些只供内部调用的带有双下划线的函数，如：
```python
def __test__(self):
    pass
```

然后再定义一些外部接口函数，让它们来调用内置函数，如：
```python
def __test__(self):
    pass
    
def test_out(self):
    return self.__test__()
```
这样更加规范和安全

### 迭代器概念

在python中，内部带有`__next__()`方法的对象都是迭代器，该对象是一个可迭代对象，在外部调用可以使用相应的内置函数`next()`

在for等循环操作开始时，会调用`可迭代对象`内部的__iter__()函数，生成一个`迭代器对象`，然后调用迭代器对象里面的__next__()方法来进行循环遍历
```python
l = [1, 2, 3, 4]

i = iter(l)  # 创建一个迭代器对象

print(next(i))
```

- 迭代协议：迭代协议分成两步，首先将一个可迭代对象使用iter()生成迭代器对象，然后对迭代器对象使用next()遍历

### zip函数

- 1.返回一个`迭代器对象`，因为它本身就是迭代器，可以直接使用next()函数

- 2.zip函数的功能是将多个序列中的元素按位置提取出来，并返回一个个元组组成的迭代器

- 3.因为zip返回的是迭代器对象，它只能被遍历`一次`

示例：
```python
l1 = [1 ,2]
l2 = (3, 4)

a = zip(l1, l2)  # 此时的a是一个迭代器对象，类似'<zip object at 0x00000134066B44C8>'的东西

print(next(a))   # 打印结果为(1, 3)

for i in a:
    print(i)     # 打印结果为(2, 4)，因为a中的第一项已经遍历过了，作为一个迭代器对象只能遍历一次，之后就只能从下一项开始
```

使用zip函数也可以很快捷的创建字典：
```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
dict1 = dict(zip(l1, l2))
print(dict1)
```

### 字符串格式化

通用格式：
```
%[(keyname)][flags][width][.precisioin]typecode
```

其中
- keyname 为索引在表达式右侧使用的字典提供键名称
- flags 罗列出说明格式的标签，如左对齐`-`，数值符号`+`，正数前的空白以及负数前的-`空格`和零填充`0`
- width 为替换的文本给出总的最小字段数
- .precision 为浮点数字设置小数点后的显示位

示例
```python
x = 1234
s1 = 'integers: ...%d ...%-6d ...%06d ...%+6d' % (x, x, x, x)
print('s1= ', s1)

y = 1.23456789
s2 = '%-6.2f | %05.2f | %+06.1f' % (y, y, y)
print('s2= ', s2)
```
输出结果为
```
s1= 'integers: ...1234 ...1234   ...001234 ... +1234'
s2= '1.23   | 01.23 | +001.2'
```

也可以使用字典的方式对字符串进行格式化
```python
s = '%(qty)d more %(food)s' % {'qty':1, 'food':'spam'}
print(s)
```
结果为
```
'1 more spam'
```

## 闭包函数（工厂函数）

闭包函数能够`记忆`外层作用域里面的值，可以用于创建函数副本，以及重写内置函数等场合

示例：
```python
def maker(n):
    def action(x):
        return x ** n
    return action
    
f = maker(2)  # 这里的f是一个函数对象
f(2)  # 结果为2的平方 4
g = maker(3)  # 另一个函数副本，计算某个数的三次方
g(2)  # 结果为2的三次方 8
# f与g是maker的两个不同副本，它们之间互不影响
```

### 使用闭包生成系列函数

因为函数本身也是一个对象，可以作为其他函数的返回值，所以可以通过函数嵌套的方式来生成系列函数，尤其是在GUI编程中对于大量相似控件生成控制函数很有帮助

示例：
```python
def MakeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i **x)
    return acts
    
acts = MakeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))
# 输出结果全为 16
```

上面的程序有一点小错误，也是循环嵌套中的一个常见陷阱：`外层作用域中的变量在嵌套的函数被调用时才进行查找`，所以当使用`acts[0](2)`等进行调用时，i的值是已经遍历完成的4，遍历过程中的i没有被记录下来

修改：
```python
def MakeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i **x)  # 为i传入一个默认值
    return acts
    
acts = MakeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))
```

修改之后，再lambda表达式中为i添加了一个默认值，因为默认值参数的求值实在嵌套函数`创建时`就发生的，所以每一个i都被记录了下来，这样就生成了一个包含不同函数对象的列表

### 定制open示例

书中有一个改写内置open函数的示例，很有趣，也更能帮助对于函数作用域和调用的理解

```python
import builtins  # 在重写的时候，为了避免出错，需要首先引用内置函数模块builtins
def makeopen(id):
    original = builtins.open   # 记忆原始函数
    def custom(*kargs, **pargs):
        print('Custom open call %r' % id, kargs, pargs)  # 增加自定义功能
        return original(*kargs, **pargs)
    builtins.open = custom  # 将open重写为custom
    
makeopen('spam')  # 调用makeopen函数，内置的open函数就被重写了
f = open('test.py')  # 此时调用的是重写之后的open函数，会打印一行自定义信息
f.read()  # open函数原有的功能仍然存在
```

