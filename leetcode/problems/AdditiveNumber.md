## 306. Additive Number

[Problem link](https://leetcode.com/problems/additive-number/)

- My approach

The key point of this problem is to find the correct beginning first and second addition number. Thecan be all the possible combinations from the start.

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # Check if the two addition numbers can add to the end
        def checkAdd(first, second, idx, start):
            if idx >= len(num) and not start:
                return True
            third = first + second
            if str(third) == num[idx:len(str(third))+idx] and num[idx] != 0:
                return checkAdd(second, third, len(str(third))+idx, False)
            else:
                return False

        for i in range(len(num)):
            first = int(num[:i+1])
            for j in range(i+1, len(num)):
                # A '0' can only be a single digit number 0 as second addition, but can't be at the start of other numbers
                if num[i+1] == '0' and j > i+1:
                    break
                second = int(num[i+1:j+1])
                if checkAdd(first, second, j+1, True):
                    return True
            # If the first number of num is 0, only 0 can be the first addition
            if num[0] == '0':
                break
        return False
```
