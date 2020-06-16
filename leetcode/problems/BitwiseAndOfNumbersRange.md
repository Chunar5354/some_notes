## Approach

[Problem link](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

- My approach

My idea is that if the right edge n is larger than (one bit higher than the hightest bit of m), the result will be 0. So we can 
narrow down the calculate range.

For example:
```
m = 50    110010
n = 100  1100100

and one bit higher than 50 is 1000000(64), 100 is larger than 64, so the result is 0
```

```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p = 1
        while m >= p:
            p <<= 1
        if n >= p:
            return 0
        res = 2147483647
        for i in range(m, n+1):
            res &= i
            if res == 0:
                return res
        return res
```

There is a very smart method from others.

- Other approach

In `AND` operation, if 0 appears once of one position, this position of result will be 0.

And as the number becomes larger one by one, all the positions will have 0 until one position that all the higher position of m and n 
are equal. And the retult will be all cleared until this position.

```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        # Find the equal position
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i
```

For example:

```
m = 5, 101
n = 7, 111

after finding the equal position: m = n = 001

and left shift two bits: 100
```
