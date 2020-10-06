## 372. Super Pow

[Problem link](https://leetcode.com/problems/super-pow/)

- Other's approach

Use recursing method, every time calculate a^b[-1].

```python
class Solution(object):
    def superPow(self, a, b):
        if len(b) == 1:
            return a ** b[0] % 1337
        return self.superPow(a, b[:-1]) ** 10 * a ** b[-1] % 1337
```

I was confused firstly that the number can only smaller than 2^64.
