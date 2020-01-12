《Python学习手册》的学习记录

* [随时记录的知识点](#%E9%9A%8F%E6%97%B6%E8%AE%B0%E5%BD%95%E7%9A%84%E7%9F%A5%E8%AF%86%E7%82%B9)
  * [通过'\#\!'创建脚本文件](#%E9%80%9A%E8%BF%87%E5%88%9B%E5%BB%BA%E8%84%9A%E6%9C%AC%E6%96%87%E4%BB%B6)
  * [查看帮助](#%E6%9F%A5%E7%9C%8B%E5%B8%AE%E5%8A%A9)
  * ['\_\_'双下划线创建内置函数](#__%E5%8F%8C%E4%B8%8B%E5%88%92%E7%BA%BF%E5%88%9B%E5%BB%BA%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0)
  * [迭代器概念](#%E8%BF%AD%E4%BB%A3%E5%99%A8%E6%A6%82%E5%BF%B5)
  * [zip函数](#zip%E5%87%BD%E6%95%B0)
  * [字符串格式化](#%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96)
* [闭包函数（工厂函数）](#%E9%97%AD%E5%8C%85%E5%87%BD%E6%95%B0%E5%B7%A5%E5%8E%82%E5%87%BD%E6%95%B0)
  * [使用闭包生成系列函数](#%E4%BD%BF%E7%94%A8%E9%97%AD%E5%8C%85%E7%94%9F%E6%88%90%E7%B3%BB%E5%88%97%E5%87%BD%E6%95%B0)
* [keyword\-only参数](#keyword-only%E5%8F%82%E6%95%B0)
  * [定制open示例](#%E5%AE%9A%E5%88%B6open%E7%A4%BA%E4%BE%8B)
* [lambda表达式](#lambda%E8%A1%A8%E8%BE%BE%E5%BC%8F)
* [推导式](#%E6%8E%A8%E5%AF%BC%E5%BC%8F)
* [生成器](#%E7%94%9F%E6%88%90%E5%99%A8)
  * [构造生成器的方式](#%E6%9E%84%E9%80%A0%E7%94%9F%E6%88%90%E5%99%A8%E7%9A%84%E6%96%B9%E5%BC%8F)
  * [yield from 语句](#yield-from-%E8%AF%AD%E5%8F%A5)
  * [关于导入](#%E5%85%B3%E4%BA%8E%E5%AF%BC%E5%85%A5)
    * [设置环境变量](#%E8%AE%BE%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
    * [动态重载](#%E5%8A%A8%E6%80%81%E9%87%8D%E8%BD%BD)
    * [隐藏变量](#%E9%9A%90%E8%97%8F%E5%8F%98%E9%87%8F)
* [类](#%E7%B1%BB)
  * [运算符重载](#%E8%BF%90%E7%AE%97%E7%AC%A6%E9%87%8D%E8%BD%BD)
    * [打印: <strong>str</strong> 和 <strong>repr</strong>](#%E6%89%93%E5%8D%B0-str-%E5%92%8C-repr)
    * [调用表达式： <strong>call</strong>](#%E8%B0%83%E7%94%A8%E8%A1%A8%E8%BE%BE%E5%BC%8F-call)
  * [类的委托：包装器类](#%E7%B1%BB%E7%9A%84%E5%A7%94%E6%89%98%E5%8C%85%E8%A3%85%E5%99%A8%E7%B1%BB)
  * [mix\-in类](#mix-in%E7%B1%BB)
    * [示例：类树列举器](#%E7%A4%BA%E4%BE%8B%E7%B1%BB%E6%A0%91%E5%88%97%E4%B8%BE%E5%99%A8)
* [装饰器](#%E8%A3%85%E9%A5%B0%E5%99%A8)
  * [函数装饰器](#%E5%87%BD%E6%95%B0%E8%A3%85%E9%A5%B0%E5%99%A8)
  * [类装饰器](#%E7%B1%BB%E8%A3%85%E9%A5%B0%E5%99%A8)



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
- 13.`isinstance(arg, type_name)`可以判断某一个变量是否为某一类型的对象
- 14.对一个实例调用`ins.__dict__`只会得到实例包含的属性，而使用`dir(ins)`除了实例的属性之外
也会得到创建实例的类中的属性以及该类所继承的全部父类中的属性
- 15.assert语句：`assert bool, 'text'`，
assert后面的bool可以是一个表达式，当其值为False时，会抛出异常，内容为text，如果值为True，则忽略这条语句继续执行
- 16.合并两个字典的方法
  - `update()`函数：d1.update(d2)，这会改变d1，
  - `d3 = {**d1, **d2}`，会得到一个新的合并后的字典d3
这两种方法当在d1和d2中出现相同键值的时候，会用d2中的值替换d1中相应键的值

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

## keyword-only参数

这类参数出现在函数定义时，参数列表中`*args`之后的有名参数:
```python
def func(a, *b, c):
    print(a, b, c)
```

在调用函数func()时，必须将参数c作为一个关键字参数来传递，否则会报错，也可以在函数定义时便为其赋予默认值:
```python
def func(a, *, b, c=1):  # 此时b和c都是关键字参数
    print(a, b, c)
```

带默认值的关键字参数在函数调用时是可选的，而不带默认值的关键字参数则必须要赋予一个值

- 注意关键字参数不能放在`**`双星号的后面

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

## lambda表达式

以表达式的形式生成一个`函数对象`，相比def语句，代码量更少，而且能够用于一些只能以表达式形式出现的场合，比如赋值

一般形式：
```python
f = lambda x,y : x+y
# f为函数名，可以没有
# lambda之后，':'前面是参数，后面是对参数要进行的运算，同时也是函数的返回值
```

## 推导式

推导式可以用来生成列表、字典以及生成器等可迭代对象，相比使用循环来实现相同的功能，使用推导式通常要快一些

常见的推导式形式：
```python
[x ** 2 for x in range(10) if x % 2 == 0]
# 生成一个元素为从0到9中偶数的平方的列表
```

## 生成器

是一个可迭代对象，但它并不一次性得出这个对象的全部内容，而是在需要的时候才产生结果，这样能够节省内存

### 构造生成器的方式

- 1.yield表达式

yield表达式用于函数定义中，将return替换成yield，带有yield表达式的函数在编译时会自动编译成一个生成器对象，如：
```python
def func():
    for i in range(5):
        yield i ** 2

y = func()
for i in range(5):
    print(next(y), end=', ')
```

输出的结果为
```
0, 1, 4, 9, 16,
```

- 2.生成器推导式

生成器推导式的语法与列表推导式类似，不过将外面的`[]`替换成了`()`，例如
```python
g = (x**2 for x in range(5))
print(g)
for i in range(5):
    print(next(g), end=', ')
```

输出的结果为：
```python
<generator object <genexpr> at 0x00000236F78E3A48>
0, 1, 4, 9, 16,
```

### yield from 语句

代替for循环等方式，等价地快速构建一个生成器：
```python
def func(n):
    for i in range(n): yield i
    for i in range(x**2 for x in range(n)): yield i
    
等价于:
def func(n):
    yield from range(n)
    yield from (x**2 for x in range(n))
```

### 关于导入

#### 设置环境变量

- 可以在命令行通过`set PYTHONPATH="path"`来设置Python的环境变量

- 也可以在程序中通过修改`sys.path`来修改，不过这种方式只能作用在本次程序运行

- 或者通过配置一个`.pth`文件来设置

#### 动态重载

使用`reload()`函数可以重载已经被import导入过的模块，可以动态地导入修改地模块

#### 隐藏变量

在模块中定义的变量名前面加上`_`可以使得这个变量在被`from module import *`这种形式导入时候被隐藏

或者可以在模块中将希望被其他文件导入时可以看见的变量存放在`__all__`列表中

但是使用下面的方式仍然可以访问被隐藏的变量：
```
import module
print(module._X)
```

## 类

### 运算符重载

这部分可以参考书P871，列举了一些常见的运算符重载方法

有几个比较常用的:

#### 打印: __str__ 和 __repr__

这两个方法都是在要将对象打印或者作为一个字符串来使用的时候被调用，区别在于：

- `__str__()`方法只在print和str()转换的时候被调用，而`__repr__()`则更为广泛

#### 调用表达式： __call__

`__call__()`方法能够把一个类的实例当作普通函数来调用，如：
```python
class Prod():
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.valu * other
        
if __name__ == '__main__':
    x = Prod(2)
    print(x(3))

# 输出结果为：
# 6
```

这里x是Prod的一个实例，而直接`x(3)`操作会调用Prod中的`__call__()`方法，返回2与3的乘积


### 类的委托：包装器类

包装器类通常通过内置方法`__getattr__()`实现，该方法会拦截对不存在属性的访问，所以通过这个方法，可以将任意的访问转发给被包装的对象，例如:
```python
class Wrapper():
    def __init__(self, obj):
        self.wrapped = obj
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

# 打印结果为：
# Trace: append
# [1, 2, 3, 4]
```

在上面的例子中，Wrapper中并没有append这个方法，却能够实现对列表元素的添加。原因在于当对调用一个不存在的属性名时，`__getattr__()`会拦截
这个属性名（attrname），并执行函数中的操作，其中`getattr(x, m)`内置方法就相当于`x.m`

### mix-in类

在我的理解，`min-in`类是定义一系列方法，并可以提供该方法给所有继承它的子类，强调通用性。书上原话是：
> mix-in类提供可通过继承向应用添加类的方法  P938

#### 示例：类树列举器

代码可查书P947。ListTree通过重载__str__()方法，可以使继承它的子类能够显示示例以及所有继承关系中的父类，帮显示他们包含的属性和方法：
```python
# File listtree.py
class ListTree():
    def __attrnames(self, obj, indent):
        spaces = ' '* (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result
    
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        # 如果该类已经访问过了
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            # 向上访问每一个父类
            for super in aClass.__bases__:
                above += self.__listclass(super, indent+4)
            return '\n{0}<Class {1}, address: {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here,
                above,
                dots)
    
    def __str__(self):
        self.__visited = {}
        # here中是实例里面的属性
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here,
            above)

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)
```

上面所引用的`testmixin.py`也是书中的示例，在P942.就是定义了一对父子类，使子类继承所传入的类参数，并进行打印：
```python
#File testmixin.py
import importlib

def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'chunar'
        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 100
        def spam(self):
            pass
    
    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)
    
def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)
```

可以自行运行`listtree.py`查看其输出结果


## 装饰器

装饰器是一个返回可调用对象的可调用对象

### 函数装饰器

可以理解为装饰器本身是一个`传入函数作为参数`的方法，它能将装饰器中包含的属性以及方法赋予被传入的函数

例子：
```python
class Tracer():
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('Class: call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('Func: call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

# When we call this function, we called just like: 
# Tracer(spam(a, b, c)), but it returns as f1()
@Tracer
def f1(a, b, c):
    return a + b + c

@tracer
def f2(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print(f1(1, 2, 3))
    print(f1('a', 'b', 'c'))
    print(f2(1, 2, 3))
    print(f2('a', 'b', 'c'))
    # print(tracer(f1(2, 3, 4)))
```

在调用一个被装饰的函数时，会将该函数以及该函数的参数都传递给装饰器代表的方法（这样的方法一般接受函数作为参数并返回一个可调用对象，
并将原来的参数与该对象绑定）

上面程序的输出为：
```
Class: call 1 to f1
6
Class: call 2 to f1
abc
Func: call 1 to f2
6
Func: call 2 to f2
abc
```

注意这个例子中的自定义装饰器，他们需要满足一些条件：
> 把一个函数当作参数并返回一个可调用对象，而原来的函数将与该对象`重新绑定`

### 类装饰器

类装饰器与函数装饰器类似 在一条class语句的末尾运行，并把一个`类名重新绑定`到一个可调用对象

使用方法为：
```python
# 需要传入一个类作为参数
def decorator(aClass):
    pass
@decorator
class C:
    pass
````

它与下列代码等价
```python
def decorator(aClass):
    pass

class C:
    pass
C = decorator(C)
```

### 装饰器的创建

创建装饰器也可以通过`函数`和`类`两种方式

#### 基于函数的函数装饰器

```python
def decorator(F):
    print('func is: ', F)
    def wrapper(*args):
        print('In wrapper', *args)
    return wrapper   # 返回的可调用对象可以不是最初传入的那个可调用对象，比如传入的是F，最终返回的是wrapper
```

它可以分别用来装饰函数和类中的方法：
```python
# 这种调用方式等价于：
# def func(x, y):
#    print('In func: ', x, y)
# decorator(func)
@decorator
def func(x, y):
    print('In func: ', x, y)
    
class C:
    @decorator
    def method(self, x, y):
        print('In class: ', x, y)
        
func(1, 2)
X = C(3, 4)
X.method()
```

输出的结果为
```
In wrapper 1 2
In wrapper 3 4
```

因为最终返回的可调用对象是装饰器函数`decorator中定义的wrapper`，所以func和method中的代码都没有被执行

#### 基于函数的类装饰器

## 异常

- Python中的异常是一个`类`，

- 如果要自定义一个异常，通常需要继承自`Exception`类

- 通过`try except`语句来捕获异常时，在except后面只要列出异常的父类，就能够捕获其对应的全部子类

- 在使用`except`抛出异常的时候，为了缩小覆盖面，最好指定异常类型，如果不确定的话就写一个错误的代码测试一下
会抛出什么样的异常，比如`IndexError`之类的

### 自定义异常类

异常类像普通的类一样可以传入参数，默认传入的参数储存在类中的`args`属性里面，作为一个元组，例如：
```python
class E(Exception): pass
try:
    raise E('test', 'second')
except E as X:
    print(X)
    print(X.args)
    print(repr(X))
```
运行该程序，输出的结果为：
```
('test', 'second')
('test', 'second')
E('test', 'second')
```

异常类也可以自定义方法，用来在出现该异常时进行相关处理，例如：
```python
class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file_):
        self.line = line
        self.file = file_
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at:', self.file, self.line, file=log)

def parser():
    raise FormatError(40, 'errorTest.txt')

if __name__ == '__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()
```

运行该程序之后，会将异常类传入的参数写入到文件`formaterror.txt`中：
```
Error at: errorTest.txt 40
```

## Unicode和字节串

Python3中字符串对象有三种类型：

- 1. str字符串，即解码的unicode文本，最为常见的字符串形式（包括ACSII）
- 2. bytes字节串，表示二进制数据（包括编码的文本）
- 3. bytearray，一种可原位修改的bytes类型

### 字符编码方案

- ACSII编码

ASCII 定义了从0到127的字符编码，将每个字符存储在8位的字节中，实际上只有7位真正用到

- 扩展：8位编码

但是有时每个字符一个字节的内存并不足以表达全部的字符，所以有一些标准使用8位字节中所有的值来表示字符，并把`非ASCII`的128~255分配给特殊字符，
如`Latin-1`字符集

- 再扩展：宽字符

有时8位的256个数也没办法完全表示字符集，这时unicode可以灵活的根据需要表示为`多个字节`。比如`utf-8`编码中，小于128的字符码表示为单个字节，
128和0x7ff（2047）之间的字符码转换为两个字节，其中每个字节的值都位于128和255之间；0x7ff以上的字符码转换为3个或4个字节序列，每个字节的值
在128和255之间。

- ASCII是Latin-1的子集，同时也是utf-8的子集

### bytes对象

Python3中的bytes对象是一个`小整数`序列（0~255）
```
>>> s = b'abcd'
>>> s[0]
97
>>> list(s)
[97, 98, 99, 100]
```

### 字符串类型转换

- 编码：根据一个期望的编码名称，把字符串翻译为原始字节形式的过程
  - str.encode()
  - bytes(s, encoding='')
- 解码：根据编码名称，把一个原始字节串翻译为字符串形式的过程
  - bytes.decode()
  - str(b, encoding='')
 
- 有一点要注意，如果在使用str方法时不指定编码名称，会返回bytes对象的`打印字符串`，而不是我们想要的str形式
```
>>> b = b'test'
>>> c = str(b)
>>> c
"b'test'"
>>> d = str(b, encoding='utf-8')
>>> d
'test'
>>> len(c)
7
>>> len(d)
4
>>>
```

### 编写Unicode字符串

为了在字符串中编写任意的，甚至在键盘上无法输入的特殊字符，Python的字符串字面量支持`\xNN`十六进制转义和`\uNNNN`与`\UNNNNNNNN`unicode转义

#### 常规的ASCII文本

常规的7位ASCII文本每个字节表示一个字符
```
>>> s = 'xyz'
>>> b = s.encode('utf-8')
>>> b
b'xyz'
>>> [c for c in b]
[120, 121, 122]
```

#### 非ASCII文本

对于非ASCII文本，可以在str字符串中通过转义字符进行转义

- `\xNN`十六进制转义，编写单个字节的值
```
>>> s = '\xc4\xe8'
>>> s
'Äè
```

- `\uNNNN`双字节Unicode转义
```
>>> s = '\u00c4\u00e8'
>>> s
'Äè'
```

- `\UNNNNNNNN`四字节Unicode转义
```
>>> s = '\U000000c4\U000000e8'
>>> s
'Äè'
```

### 文件中的BOM序列

一些编码方式在文件的开始处存储了一个特殊的字节顺序标记（BOM）序列，来指定数据的大小尾方式（字符串哪一端的位对其值更加重要）或声明编码类型

- 在`utf-8`中，使用更为特定的编码名称`utf-8-sig`编码名称会在输入和输出的时候分别跳过和写入BOM，常规的utf-8不会这样做

比如打开一个带有3字节UTF-8 BOM序列的文本文件`test`
```
>>> open('test', 'rb').read()
b'\xef\xbb\xbftest1\r\ntest2\r\n'
>>> open('test', 'r').read()
'锘縯est1\ntest2\n'
>>> open('test', 'r', encoding='utf-8').read()
'\ufefftest1\ntest2\n'
>>> open('test', 'r', encoding='utf-8-sig').read()
'test1\ntest2\n'
>>>     
```

- 在`utf-16`中，总是进行BOM处理，还可以使用`utf-16-le`来指定小尾格式，`utf-16-be`指定大尾格式
  - utf-16并不常用，所以在此不给出例子，详细内容参考书中`P1172`
