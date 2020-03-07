## Approach

[Problem link](https://leetcode.com/problems/decode-ways/)

- My approach

My recursing method was time exceeded again. It's important to use memory in recursing funciton.

- Other's approach

The best way to solve this problem is calculating ways of current number, which equals to (use one number to represend a letter) plus 
(use two numbers to represend a letter(only the number is smaller than 26)).

And it can be recursing and just traverse.

```python
class Solution:
    def __init__(self):
        self.memo={}
        
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)
    
    def recursive_with_memo(self, index, s) -> int:
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        if index in self.memo:
            return self.memo[index]
        # The ways of current number
        ans = self.recursive_with_memo(index+1,s) +\
            (self.recursive_with_memo(index+2,s) if (int(s[index:index+2])<=26) else 0)
        # Save it into memory
        self.memo[index]=ans
        
        return ans
```

And the un-recursing one is a little difficult to understand.

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        prev = 1
        last = 1
        cur = last
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or int(s[i-1:i+1]) >26: return 0
                cur = prev
            elif s[i-1] == '0' or int(s[i-1:i+1]) > 26:
                cur = last
            else:
                cur = prev + last
            prev = last
            last = cur
        return cur        
```
