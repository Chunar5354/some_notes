## Approach

[Problem link](https://leetcode.com/problems/factorial-trailing-zeroes/)

- My approach

How many zeros at thr end of factorial depends on the given number contains how many `i` of `5^i`.

For example

```
If the given number is 10:
  because 10 contains two `5`, 10 can add a zero to the end of factorial, so does 5*2
If the given number is 100:
  100 contains 20 '5' which can add a zero, and 4 '25' which can add 2 zeros
```

So the code should be:

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 1
        res = 0
        while 5**i <= n:
            res += n // 5**i
            i += 1
        return res
```
