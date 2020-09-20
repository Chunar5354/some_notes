## 343. Integer Break

[Problem link](https://leetcode.com/problems/integer-break/)

- My approach

The maximum product must be: divide n equally to k parts, and max((n/k)^k for k in range(sqrt(n)).

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        e = int(n**0.5)
        res = 0
        # 2 and 3 are special
        if n == 2:
            return 1
        if n == 3:
            return 2
        for i in range(1, e+2):
            p = n // i
            r = n % i
            # for example, if n=10, we can divide it to 3+3+4 or 3+3+3+1, so there are two answers, we take the larger one
            res = max(res, i**p*r, i**(p-1)*(r+i))
        return res
```

- Dynamic programming

This problem can also be solved by dynamic programming.

For current dp[i], dp[i-k] stands for the maximum product of i-k, so the maximum product of i will be max(k*dp[i-k], k*(i-k)).

There are only two base numbers 2 and 3, all the numbers after 3 can be calculated from the base number.

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if(n <= 2): return 1
        dp = [0,0,1,2]                          # base cases for 2,3
        for i in range(4, n + 1):
            dp.append(max( max(3 * dp[i - 3], 3 * (i - 3)), max(2 * dp[i - 2], 2 * (i - 2)) ))         # appending to dp list
        return dp[n]
```
