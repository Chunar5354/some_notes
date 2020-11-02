## 397. Integer Replacement

[Problem link](https://leetcode.com/problems/integer-replacement/)

- My approach

Recursing method:

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        self.res = float('inf')
        def helper(num, step):
            if num == 1:
                self.res = min(self.res, step)
                return
            if num % 2 == 0:
                helper(num//2, step+1)
            else:
                helper((num+1)//2, step+2)
                helper((num-1)//2, step+2)
        
        helper(n, 0)
        return self.res
```

Recursing with memory:

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        self.dp = {}
        
        def helper(num):
            if num == 1:
                return 0
            if num in self.dp:
                return self.dp[num]
            if num % 2 == 0:
                self.dp[num] = helper(num//2) + 1
            else:
                self.dp[num] = min(helper((num-1)//2), helper((num+1)//2)) + 2
            return self.dp[num]
        
        res = helper(n)
        return res
```
