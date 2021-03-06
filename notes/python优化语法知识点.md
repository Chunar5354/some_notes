## python中“*”

`*`在函数定义中可以用来表示可接受多个参数，`*`后面的变量默认为一个元组，如下例中的args

```python
def fun(a, *args):
    print(a)
    print(args)
list = [1, 2, 3, 4]
fun(1, list)
```

这部分代码的输出结果为

```
1, (1, 2, 3, 4)
```

`*`符号会将列表中的元素进行拆分遍历，然后保存在args元组中

除了函数定义，在其他地方，`*`也可以表示拆分遍历，后面的参数可以是任何形式的数组，如元组、列表或字典

```python
a = (1, 2, 3)
print(*a)

# 输出：1, 2, 3

a = [1, 2, 3]
print(*a)

# 输出：1, 2, 3

a = {'a': 1, 'b': 2, 'c': 3}
print(*a)

#输出：a, b, c
#注意参数是字典的时候，输出的只有键
```

## python中“**”

`**`在python中用于解析字典，在函数定义中**后面的参数默认为一个字典，写入是要有“=”符号：

```python
def fun(a, **kwargs):
    print(a)
    print(kwargs)
    
fun(1, b=2, c=3)
```

输出的结果为：

```
1
{'b': 2, 'c': 3}
```

在函数定义之外，`**`可以用来拆分字典中的键值对：

```python
def fun(a, **kwargs):
    print(a)
    print(kwargs)
    
fun(1, **{'b': 2, 'c': 3})
# 这里在调用函数传入参数的时候，如果不加上'**'，则会认为是一个字典类型的位置参数
# 加上了'**'之后，则会将字典中的键值对进行解析，等同于“b=2, c=3”
```

运行上面的代码，输出：

```
1
{'b': 2, 'c': 3}
```
