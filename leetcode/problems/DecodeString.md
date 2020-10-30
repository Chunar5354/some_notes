## 394. Decode String

[Problem link](https://leetcode.com/problems/decode-string/)

- My approach

Use recursing method, and deal with the substring in `[]` as a new string.

```python
class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(st):
            i = 0
            res = ''
            while i < len(st):
                if st[i] in '1234567890':
                    num = 0
                    while st[i] in '1234567890':
                        num = num*10 + int(st[i])
                        i += 1
                    # inBracket[0] is the substring in '[]', inBracket[1] is the index of the end of ']'
                    inBracket = helper(st[i+1:])
                    res += num * inBracket[0]
                    i += inBracket[1]+1  # calculate the next index
                elif st[i] not in '1234657890' and st[i] != ']':  # common characters
                    res += st[i]
                    i += 1
                elif st[i] == ']':  # ']' means one substring is over
                    return (res, i+1)
            return (res, i+1)
            
        return helper(s)[0]
```

- Other's approach

We can also solve this problem by iterator method with stack.

The key point is: for nested brackets, when we solve one bracket, add it back to stack, so it can be added into the larger bracket.

```python
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        i = 0
        res = ''
        for i in s:
            if i == ']':
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                num = ''
                while stack and stack[-1] in '1234567890':
                    num = stack.pop() + num
                for c in int(num) * curr:  # add the string back to stack
                    stack.append(c)
            else:
                stack.append(i)
        
        return ''.join(stack)

```
