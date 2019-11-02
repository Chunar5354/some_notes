## 解题

[题目链接](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

这个自己没做出来，写的代码都超时了，想的方法是比较傻的挨个遍历，首先用集合找到所有出现的字符，
然后字符串的最大长度就是字符数，并按照长度逐个遍历，最终执行超时了：
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        m_list = []
        s_set = set(s)
        n = len(s_set)
        if n == len(s):
            return n
        else:
            while n > 0:
                for i in range(len(s) - n + 1):
                    s_sub = s[i: i+n]
                    print(i, n)
                    if len(set(s_sub)) == len(s_sub):
                        m_list.append(len(s_sub))
                n = n - 1
            return max(m_list)
```

然后优化的办法怎么也没想出来，就查看了其他人的答案，一个比较清晰的:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                # 每当出现重复字符的时候，结果字符串就从第一个重复字符串的下一个字符开始
                str_list = str_list[str_list.index(x)+1:]
            str_list.append(x)    
            # print(str_list)
            max_length = max(max_length, len(str_list))  # 中途记录最长的结果字符串
        return max_length
```

它顺序遍历所有字符，并存放在一个列表中，每当出现重复字符的时候，结果字符串就从第一个重复字符串的下一个字符开始，例如`abcda`，执行到第二个a的时候，
就将列表更新为`['b', 'c', 'd', 'a']`，列表中永远不会出现重复，并在途中记录结果字符串长途的最大值

还有一种更快速的方法，使用字典，实现的思想与上面类似：
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):   # 取字符和其对应的索引
            if i in dct and dct[i] >= start:   # 如果出现了重复元素
                max_so_far = max(max_so_far, curr_max)   # 记录最长字符串
                curr_max = index - dct[i]   # 长度为两个重复字符串之间的间隔
                start = dct[i] + 1   # start表示从第几个字符开始作为结果字符串，在判断的时候，出现的重复字符串如果在start之前就不算了
            else:
                curr_max += 1   # 如果字符没出现在dct中，结果字符串长度要加1
            dct[i] = index    # 把每个字符都存到dct中
        return max(max_so_far, curr_max)
```

它也是顺序遍历字符串，并按照`{value: index}`的格式将字符串的每个字符存放在一个字典中，每当出现重复字符，结果字符串的长度即为两个
重复字符串之间的`位置差`，并且使用了一个`start`变量来表示结果字符串的起始位置，如果在遍历中找到的重复字符串的位置在start之前，就忽略这个字符
并且在每一次遍历中都更新当前字符在字典中存储的索引值

### 结论

- 1.像这种查找多个元素的最大值问题，一般要在每一次的查找中进行比较，记录最大值
- 2.使用字典反向存储一个列表或者字符串的value和index的关系往往起到很好的作用
- 3.这个问题的关键是在每次出现重复字符的时候，要更新结果字符串的`第一个字符`


## 知识点

- 滑动窗口，类似于上面解法2中的列表[i, j]，当每次出现元素k与[i, j]中的元素相同的时候，窗口就变为[k+1, j]

