## Approach

[Problem link](https://leetcode.com/problems/sqrtx/)

- My approach

Using a method like binary search, every time find the middle of current number and last number, until find the number
(n**2 <= x).

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        n = x // 2
        last_left_n = 0
        last_right_n = n
        while True:
            if n ** 2 > x:
                # Record current n as larger n
                last_right_n = n
                # Next n is half of (current_n + smaller_n)
                n = (n+last_left_n) // 2
            elif n ** 2 < x:
                if (n+1) ** 2 > x:
                    break
                if (n+1) ** 2 == x:
                    n += 1
                    break
                # Record current n as smaller n
                last_left_n = n
                # Next n is half of (current_n + larger_n)
                n = (n+last_right_n) // 2
            elif n ** 2 == x:
                break
        return n
```

And there is a magic method.
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        while a * a > x:
            a = (a + x // a) // 2
        return a
```

The judging condition can be expressed as a mathematical formula `a < sqrt(x) < x/a` or `a > sqrt(x) > x/a`, where `a` is a number 
that smaller than x. And at one certain time, only one of the two formulas can be successful(depends on the value of a).

Explanaion:
```
if a < sqrt(x):
  1/a > 1/sqrt(x)
  x/a > x/sqrt(x)
  x/a > sqrt(x)
so a < sqrt(x) < x/a

if a > sqrt(x):
  1/a < 1/sqrt(x)
  x/a < x/sqrt(x)
  x/a < sqrt(x)
so a > sqrt(x) > x/a
```
