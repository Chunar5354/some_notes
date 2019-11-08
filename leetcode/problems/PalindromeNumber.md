## 解题

[题目链接](https://leetcode.com/problems/palindrome-number/)

这道题比较简单，如果用字符串的方法一行代码就搞定了:
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
```

不过题目中给了一个提高项目：不使用字符串方法。那就逐位取余，再反向加和：
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        sou = x
        while sou > 0:
            # 取sou除以10的商和余数
            sou, rem = divmod(sou, 10)
            res = res * 10 + rem
        if res == x:
            return True
        else:
            return False
        # 其实后面的判断没有必要，对于返回值要求是bool的时候，可以直接return
        # return res == x
```

运行速度也很快，超过85%

不过官方解答中给出了一个更优化的方案：反向加和没必要加完整个数字，只要处理到数字长度的一半就可以了，因为回文数字后一半的倒置和前一半一定相等，
对于长度为奇数的数字，加完一半之后除以10去掉个位就好了：
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        res = 0
        while x > res:
            x, rem = divmod(x, 10)
            res = res * 10 + rem
        # 判断：前一半针对偶数长度的数字，后一半针对奇数长度
        return x == res or x == res // 10
```

### 结论

- 1.对于返回值为bool的函数，可以直接return表达式
- 2.对于回文，可以只取一半进行处理，节约资源
