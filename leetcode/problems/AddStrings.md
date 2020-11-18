## 415. Add Strings

[Problem link](https://leetcode.com/problems/add-strings/)

- My approach

Add the numbers bit by bit with carry.

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # form into same length
        if len(num1) > len(num2):
            num2 = '0'*(len(num1)-len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = '0'*(len(num2)-len(num1)) + num1

        res = ''
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            curr = int(num1[i]) + int(num2[i]) + carry
            if curr >= 10:
                carry = 1
                res = str(curr%10) + res
            else:
                carry = 0
                res = str(curr) + res
        if carry > 0:
            return '1'+res
        return res
```
