## 393. UTF-8 Validation

[Problem link](https://leetcode.com/problems/utf-8-validation/)

- My approach

Use `bin()` to converse numbers into binary string, and check them by the given rules.

```python
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        d = [n&255 for n in data]
        i = 0
        while i < len(d):
            if d[i] < 128:  # d[i]<128 means it starts with 0
                i += 1
            else:
                b = bin(d[i])[2:]
                if b[:2] == '10':  # '10' can only follow with `11x`
                    return False
                j = 0  # the count of 1 
                while j < len(b) and b[j] == '1':
                    j += 1
                if j > 4:  # there can be at most 4 bytes
                    return False
                for k in range(1, j):  # all the j-1 numbers followed must start with '10'
                    if i+k > len(d)-1 or d[i+k] < 128 or bin(d[i+k])[2:4] != '10':
                        return False
                i += j
        return True
```
