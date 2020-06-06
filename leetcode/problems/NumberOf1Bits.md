## Approach

[Problem link](https://leetcode.com/problems/number-of-1-bits/)

- My approach

Use bit shift to check every bit.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # Using and method to check only the last bit
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res
```

- Official approach

In binary numbers, `n and n-1` will clear all the bits after the last `1`. For example:

```
n  =  01100100
n-1 = 01100011
n and n-1 = 01100000
```

We can use this to clear the last `1` step by step until n becomes 0.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & n-1
            res += 1
        return res
```
