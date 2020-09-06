## 326. Power of Three

[Problem link](https://leetcode.com/problems/power-of-three/)

- My approach

Multiply 3 until num is larger or equal to n. Then check if num equals to n.

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        return math.log(n, 3) % 1 == 0
```

Or using `log` to calculate the logarithm of n-3. If n is a power of 3, the logarithm will be an integer.

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return math.log10(n) / math.log10(3) % 1 == 0
```

Attention here, using math.log(n, 3) may cause float overflow. For example, the result of math.log(243, 3) is 4.99999.
