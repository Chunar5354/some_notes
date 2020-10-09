## 375. Guess Number Higher or Lower II

[Problem link](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)

- Other's approach

Use 2D cache and search by recursing. 

For every number, the cost will be the cost of guessing the numbers smaller current plus guessing the numbers larger than current plus current number(cost).

```python
class Solution:
    def getMoneyAmount(self, n):
        cache = [[0]*(n+1) for _ in range(n)]
        def guess(lo, hi):
            if lo >= hi:  # lo==hi means find the target, this will cost 0
                return 0
            if cache[lo][hi] > 0:
                return cache[lo][hi]
            ret = float('inf')
            for i in range((lo+hi)//2, hi):
                t= i + max(guess(lo, i-1),guess(i+1, hi))  # smaller numbers + larger numbers + current number
                ret = min(ret, t)
                
            cache[lo][hi] = ret
            return ret
        res = guess(1, n)
        return res
```
