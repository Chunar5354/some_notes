## 405. Convert a Number to Hexadecimal

[Problem link](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)

- My approach

For negative number m, the two's complement equals to `2^32 + n`.

Every time divide the number by 16, and add the remainder at the front of result.

```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = 2**32 + num
        dic = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        res = ''
        while num > 0:
            curr = num % 16
            num = num // 16
            if curr < 10:
                res = str(curr) + res
            else:
                res = dic[curr] + res
        return res
```
