## 374. Guess Number Higher or Lower

[Problem link](https://leetcode.com/problems/guess-number-higher-or-lower/)

- My approach

Use binary search.

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        num = (l+n) // 2
        while guess(num) != 0:
            if guess(l) == 0:
                return l
            if guess(n) == 0:
                return n
            if guess(num) == 1:
                l = num
            elif guess(num) == -1:
                n = num
            num = (l+n) // 2
        return num
```
