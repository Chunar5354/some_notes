## 解题

[题目链接](https://leetcode.com/problems/zigzag-conversion/)

又自然而然的想到了用字典储存列表的方法，将zigzag之后的每一行都存放在一个列表中，最后按顺序拼接在一起，关键在于计算每一行元素的共同特征：
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 首先按照给出的行数numRows创建一个列表：{0: [], ... numRows: []}
        res_dict = {i: [] for i in range(numRows)}
        n = 2 * (numRows-1)  # 元素的特征之一是相邻的元素位置相差n（第一行和最后一行）
        for i in range(len(s)):
            do_fin = 0
            n1 = (i + n) % n
            # 除了第一行和最后一行，其他每一行的元素有两个序列，一个是从n1开头，一个是从n2开头，各自的间隔都是n
            # n2和n1的关系是 n2 = n - n1
            n2 = n - n1
            # 从左至右把每个元素插入对应的列表中
            if n1 in res_dict:
                res_dict[n1].append(s[i])
                do_fin = 1
            if n2 in res_dict and do_fin == 0:
                res_dict[n2].append(s[i])
        print(res_dict)
        res_list = []
        for key in res_dict:
            res_list += res_dict[key]
        return ''.join(res_list)
```

大方向没问题，基本上是一把过，但是成绩仍然不太理想（20%）

参考了高分代码，人家没有用索引值计算，而是比较机智的利用了zigzag的走向特征，创建了一个`方向`变量，其他的也是一次添加到列表中：
```python
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        step = 1  # 表示zigzag的方向是向上走还是向下走
        pos = 1
        lines = {}
        for c in s:
            if pos not in lines:
                lines[pos] = c
            else:
                lines[pos] += c
            pos += step  # 走一步
            if pos==1 or pos==numRows:   # 如果走到头或走到尾，就改变方向
                step*=-1
        sol = ""
        for i in range(1, numRows):
            try:
                sol+=lines[i]
            except:
                return sol
        return sol
```

一个更快速的版本：
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):return s
        ret_res = [''] * numRows   # 他这里直接用列表存放了每一行的字符串
        i_b = 0
        for c in s:
            if i_b == 0:inc = 1  # 依然是方向
            elif i_b == numRows - 1:inc = -1  # 依然是方向
            ret_res[i_b] += c
            i_b += inc  # 走一步
        return ''.join(ret_res)
```

### 结论

- 对于zigzag这种来回循环的问题，引入一个`方向`的点子真是太赞了

## 知识点

- zigzag：之字形结构
