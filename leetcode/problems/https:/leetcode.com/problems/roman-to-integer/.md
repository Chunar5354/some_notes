## 解题

[题目链接](https://leetcode.com/problems/roman-to-integer/)

这个题和[integer-to-roman](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/IntegerToRoman.md)类似，先用一个字典储存数值和字符的对应关系，再进行遍历即可：
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1,
             'V': 5,
             'IV': 4,
             'X': 10,
             'IX': 9,
             'L': 50,
             'XL': 40,
             'C': 100,
             'XC': 90,
             'D': 500,
             'CD': 400,
             'M': 1000,
             'CM': 900}
        res = i = 0
        while i < len(s):
            if s[i: i+2] in d:
                res += d[s[i: i+2]]
                i += 1
            else:
                res += d[s[i]]
            i += 1
        return res
```

一开始先把字符串给反转过来了，其实没必要，反正是加一个总和，一把成，没啥难点
