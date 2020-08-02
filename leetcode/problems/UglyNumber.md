## 263. Ugly Number

[Problem link](https://leetcode.com/problems/ugly-number/)

- My approach

Check if 2, 3 or 5 is a factor of num, and if true, divide num with the factor and modify it.

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            if num % 5 == 0:
                num = num // 5
            elif num % 3 == 0:
                num = num // 3
            elif num % 2 == 0:
                num = num // 2
            else:
                return False
        return True
```
