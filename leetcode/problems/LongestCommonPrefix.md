## 解题

[题目链接](https://leetcode.com/problems/longest-common-prefix/)

寻找字符串前缀，python中有一个很方便的函数`startswith()`，对每一个字符进行遍历即可：
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        p = ''
        for i in range(len(strs[0])):
            all_pass = True
            p = strs[0][: i+1]
            print(p)
            for j in range(len(strs)):
                if not strs[j].startswith(p):
                    all_pass = False
                    break
            # all_pass 的值为 False说明没有全部通过，那么前缀就是上一个p，也就是p[: -1]
            if not all_pass:
                p = p[: -1]
                break
        return p
```

不过`startswith()`毕竟是python内置的方法，自己来写一个通用的方法可能更好一些，那就逐位去判断每个字符串的对应位置字符是否相等
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        num = 0
        for i in range(len(strs[0])):
            all_pass = True
            p = strs[0][i]
            print(p)
            # 判断每个字符串的第i位是否相等
            for j in range(len(strs)):
                try:
                    if strs[j][i] != p:
                        all_pass = False
                        break
                # 如果后面的字符串比第一个字符串长，则会产生一个超出索引范围的异常
                # 这也意味着当前的前缀字符strs[0][p]不是共同的前缀，置all_pass为False
                except:
                    all_pass = False
                    break
            if not all_pass:
                num = i
                break
            # 如果all_pass为True，说明当前的前缀字符strs[0][p]是共同的前缀，更新索引值，继续判断下一个字符
            num = i + 1
        return strs[0][: num]
```

自己重写的方法反而比startwith()更快了（超过99%）
