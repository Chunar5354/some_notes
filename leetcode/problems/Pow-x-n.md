## Approach

[Problem link](https://leetcode.com/problems/powx-n/)

- My approach

We can directly use `**` method to calculate the power.
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return round(x**n, 5)
```

And we can use a recursing-binary-search method.
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        # A recursing function
        def traceback(ans, t):
            quo = t // 2
            if quo >= 1:
                diff = t - quo * 2
                # The answer is (ans^2)^quo--(diff=0)
                # or ans*((ans^2)^quo)--(diff=1)
                if diff == 0:
                    return traceback(ans*ans, quo)
                else:
                    return ans*traceback(ans*ans, quo)
            else:
                return ans
        return traceback(x, n)
```
