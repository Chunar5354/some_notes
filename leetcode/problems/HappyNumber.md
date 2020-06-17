## Approach

[Problem link](https://leetcode.com/problems/happy-number/)

- My approach

The key point is if the number is not a happy number, during the calculating there will be duplicated numbers.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while True:
            nums = []
            # Calculate next number
            while n > 0:
                nums.append(n%10)
                n = n // 10
            n = sum(i**2 for i in nums)
            if n == 1:
                return True
            # If there is duplicated number, it's not a happy number
            if n in mem:
                return False
            mem.add(n)
```
