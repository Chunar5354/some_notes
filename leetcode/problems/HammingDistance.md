## 461. Hamming Distance

[Problem link](https://leetcode.com/problems/hamming-distance/)

- My approach

Count bit by bit.

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x > 0 and y > 0:
            xi = x % 2
            yi = y % 2
            x = x // 2
            y = y // 2
            if xi != yi:
                res += 1

        while x > 0:
            xi = x % 2
            x = x // 2
            if xi != 0:
                res += 1
        while y > 0:
            yi = y % 2
            y = y // 2
            if yi != 0:
                res += 1
        return res
```

- Other's approach

Firstly calculate `n=(x^y)`(XOR), the counte of bit 1 in n is the different bits of x and y.

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
```

