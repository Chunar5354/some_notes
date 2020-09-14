## 335. Self Crossing

[Problem link](https://leetcode.com/problems/self-crossing/)

- Other's approach

The key point is run two more steps than a square. So there are 6 sides.

See the [explanation](https://leetcode.com/problems/self-crossing/discuss/79141/Another-python...)

```python
class Solution:
    def isSelfCrossing(self, x):
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            # Every time move one step
            b, c, d, e, f = a, b, c, d, e
        return False
```
