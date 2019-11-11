## 解题

[题目链接](https://leetcode.com/problems/integer-to-roman/)

数字转换成罗马数字，本质上是数字和字符串的一一对应，只要掌握各自的规则再进行拼凑就可以了：
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义一个字典存放对应的字符
        d = {0: 'IV',
             1: 'XL',
             2: 'CD',
             3: 'M'}
        # 这里的b表示个十百千的位数，后面会用到
        b = 0
        s = ''
        # b<3表示超过1000的部分就不适用下面的运算
        while num > 0 and b < 3:
            num, rem = divmod(num, 10)
            if rem < 4:
                sub_s = d[b][0] * rem
            elif rem == 4:
                sub_s = d[b]
            elif rem > 4 and rem < 9:
                sub_s = d[b][1] + d[b][0] * (rem - 5)
            else:
                sub_s = d[b][0] + d[b+1][0]
            s = sub_s + s
            # 每次b加1表示表示下一次处理更高一位，对应字典d中的键
            b += 1
        if num > 0:
            sub_s = num * d[3]
            return sub_s + s
        else:
            return s
```

运行速度很快（超过97%），但是这种想法拐了太多弯了，有点复杂，下面是一个别人的答案：
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        rm = ((1000, 'M'), 
              (900, 'CM'),
              (500, 'D'), 
              (400, 'CD'), 
              (100, 'C'), 
              (90, 'XC'), 
              (50, 'L'), 
              (40, 'XL'), 
              (10, 'X'), 
              (9, 'IX'), 
              (5, 'V'), 
              (4, 'IV'), 
              (1, 'I'))
        # 对num从大到小进行除运算，再从num中减掉被运算过的部分
        for i, m in enumerate(rm):
            q, r = divmod(num, m[0])
            s += m[1] * q
            num -= q * m[0]
        return s
```

他是把所有可能出现的字符串类型都存在了一个元组中，再按照这些字符串对应的数值从大到小的顺序，每次都去掉包含最大数值的部分，
再把剩下的数跟小数值进行运算，一直算到`1`，这种方法速度上稍微慢了一点点（因为对每个num都要完整的遍历元组rm），但是非常简洁和直接

### 结论

- 对于整数的处理，有时候可以试试从`高位到低位`计算的顺序
- 字典还是香啊
