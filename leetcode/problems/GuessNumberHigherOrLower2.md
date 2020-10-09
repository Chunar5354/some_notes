## 375. Guess Number Higher or Lower II

[Problem link](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)

- Other's approach

Use 2D cache and search by recursing. 

```python
class Solution:
    def getMoneyAmount(self, n):
        cache = [[0]*(n+1) for _ in range(n)]
        def guess(lo, hi):
            if lo >= hi:
                return 0
            if cache[lo][hi] > 0:
                return cache[lo][hi]
            ret = float('inf')
            for i in range((lo+hi)//2, hi):
                t= i + max(guess(lo, i-1),guess(i+1, hi))
                ret = min(ret, t)
                
            cache[lo][hi] = ret
            return ret
        res = guess(1, n)
        return res
```
