## 342. Power of Four

[Problem link](https://leetcode.com/problems/power-of-four/submissions/)

- My approach

The simplest solution is loop.

```python
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        n = 1
        while n < num:
            n *= 4
        return n == num
```

- Other's approach

If we don't use loop, we can solve this problem by bit method.

We can see that if a number is power of 4, there can only be one 1 in the binary bits, and it must be at the positions like `'10'*n + 100` such as 100(4), 10000(16), 1000000(64).

```python
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        
        decisor = int("1010101010101010101010101010100", 2)
        tmp = bin(num)[2:]

        if decisor | num == decisor and tmp.count("1") == 1:
            return True
        else:
            return False
```
