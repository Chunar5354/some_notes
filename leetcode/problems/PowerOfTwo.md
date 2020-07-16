## 231.Power of Two

[Problem link](https://leetcode.com/problems/power-of-two/)

- My approach

This is an easy problem, just mutiply with 2 each time and compare with target number n. If current number is larger than n, return false.

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while True:
            if num == n:
                return True
            if num > n:
                return False
            num *= 2
```

But the more smart method is to divide the target n by 2 and check the remainder, this can run faster.

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <1:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True
```
