## 258. Add Digits

[Problem link](https://leetcode.com/problems/add-digits/)

- My approach

My idea is adding the digits explicitly.

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            _sum = 0
            while num > 0:
                _sum += num % 10
                num = num // 10
            num = _sum
        return num
```

- Official solution

There is a regular that the sum of digits in a number equals to the mod of 9. So we can solve this problem in the mathimatical way.

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
```

