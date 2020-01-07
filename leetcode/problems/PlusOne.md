## Approach

[Problem link](https://leetcode.com/problems/plus-one/)

- My approach

The first approach is transform list into an integer, then plus one, and transform the integer back to a list.
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits)):
            n = len(digits) - i - 1
            number += digits[n] * 10 ** i
        number += 1
        res = []
        while number > 0:
            num = number % 10
            res = [num] + res
            number = number // 10
        return res
```

And the second approach is plus on the list itself.
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Considering carry, firstly add a '0' at the start of list
        digits = [0] + digits
        for i in range(len(digits)):
            n = len(digits) - i - 1
            digits[n] += 1
            # If current sum equals to 10, it needs to do a carry
            if digits[n] == 10:
                digits[n] = 0
            else:
                break
        # Finally delete the '0' at beginning
        j = 0
        while digits[j] == 0:
            j += 1
            
        return digits[j:]
```
