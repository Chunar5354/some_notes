## 441. Arranging Coins

[Problem link](https://leetcode.com/problems/arranging-coins/)

- My approach

Start from sqrt(2n), because we can calculate by `x(x-1)/2 = n`, x is close to and smaller than sqrt(2n).

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = int((2*n)**0.5)
        while x > 0:
            if x*(x+1)//2 <= n:
                return x
            x -= 1
        return x
```
