## 解题

[题目链接](https://leetcode.com/problems/longest-palindromic-substring/)

一开始没读透`回文(palindromic)`的意思，顺着`Longest Substring Without Repeating Characters`这道题的思路写了。
发现错误之后又经过艰苦卓绝的奋斗，独立搞出来了，而且分数竟然很高（超过90%）：
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Set a dict, the structure is {char: [index1, index2, ...]}
        When finding a repeated char, check if the string between the same chars is palindromic
        '''
        res_dict = {}
        max_n = max_all = 0
        if len(s) > 0:
            max_s = s[0]
        else:
            return ''
        for index, val in enumerate(s):
            if val not in res_dict:
                res_dict[val] = [index]
            else:
                # add the index into dict
                res_dict[val].append(index)
                for i in range(len(res_dict[val])):
                    max_n = index - res_dict[val][i] + 1
                    cur_s = s[res_dict[val][i]: index+1]
                    if cur_s == cur_s[::-1]:
                        if max_n > max_all:
                            max_all = max_n
                            max_s = cur_s
                        break
        return max_s
```

思路是`找重复字符`，并将相同字符的每一个位置（索引值）存放在一个列表中，并使用`{char: [index1, index2, ...]}`结构的字典来存储，
每当找到重复的字符时，先判断两个最远重复字符（index1）之间的字符串是否为回文，如果不是，再判断第二远重复字符（index2），以此类推，
并在中途记录最长的回文字符串

后来又找了一个答案中最快的程序，研究一下没太懂（但是他比我的快10几倍），先把这个神仙程序记录下来：
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s[::-1] == s:
            return s
        start = 0
        max_len = 1
        
        for i in range(len(s)):
            i_odd = i - max_len -1
            i_even = i - max_len
            odd = s[i_odd:i+1]
            even = s[i_even:i+1]
            print(odd, even)
            if i_odd >= 0 and odd == odd[::-1]:  # 为什么长度要分加1和加2？
                max_len += 2
                start = i_odd
            if i_even >=0 and even == even[::-1]:
                max_len += 1
                start = i_even
        return s[start:start+max_len]
```

### 结论

- 找回文字符串，判断其正反向是否相等是一个好办法

## 知识点

- Python中倒序：通过`[::-1]`的方法，可以处理如字符串和列表等有序的序列，例如：
```python
a = 'abcd'
print(a[::-1])
# 结果为： dcba
```

也可以从中间某一元素开始倒序排列，`[2::-1]`表示从下标为2的元素开始倒序排列，例如：
```python
a = 'abcd'
print(a[2::-1])
# 结果为： cba
```
