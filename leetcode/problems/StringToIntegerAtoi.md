## 解题

[题目链接](https://leetcode.com/problems/string-to-integer-atoi/)

这道题没有太大的含金量啊，就是没啥知识点（官方连答案都没给），关键在于如何找到目标字符串：
```python
class Solution:
    def myAtoi(self, str: str) -> int:
        dig_s = ' -+0123456789'
        # start_i表示第一个出现`-+0123456789`中字符的位置
        # end_i表示start_i出现之后，最近的一个非数字字符出现的位置
        start_i = end_i = -1
        for i in range(len(str)):
            if str[i] not in dig_s and start_i == -1:
                return 0
            if str[i] not in dig_s[3:] and start_i != -1:
                end_i = i
                break
            if str[i] in dig_s[1:] and start_i == -1:
                start_i = i

        # 如果到最后都没有出现start_i和end_i
        if start_i == -1:
            return 0
        if end_i == -1:
            end_i = len(str)
            
        s = str[start_i:end_i]
        if s == '-' or s == '+':
            return 0
        n = int(s)
        if n >= 2147483647:
            return 2147483647
        if n <= -2147483648:
            return -2147483648
        return n
```

自己的答案超过了47%，还算可以

看了高分的答案，他用了一个比较巧妙的方法先去掉了开头的空格字符，然后对每个字符调用`int()`方法，通过抛出异常来检测目标字符，省去了多次遍历：
```python
class Solution:
    # 去掉字符串开头的空格
    def remove_ws(self, s):
        new_s = ""
        ignore_ws = True
        
        for char in s:
            if char != " ":
                ignore_ws = False
            
            if char == " " and ignore_ws == True:
                continue
                
            new_s += char
        return new_s
    
    def myAtoi(self, s: str) -> int:
        s = self.remove_ws(s)      
        
        is_negative = s.startswith("-")
        if is_negative or s.startswith("+"):
            s = s[1:]
        
        num_str = ""
        for i in s:
            try:
                int(i)  # 在遇到非数字字符时会出错，抛出异常，从而终止遍历
                num_str += i
            except ValueError:
                break
                
        if num_str == "":
            return 0
        
        num =  0 - int(num_str) if is_negative else int(num_str)
        
        if num < -2147483648:
            return -2147483648
        
        if num >= 2147483648:
            return 2147483647
        
        return num
```

### 结论

- 1.答案二中去掉开头空格字符的方法值得借鉴
- 2.有时候可以利用Python的异常机制
