## 457. Circular Array Loop

[Problem link](https://leetcode.com/problems/circular-array-loop/)

- My approach

There are two points for a loop:

1. The numbers must be all positive or negative

2. Ther can't be only one number's loop(when a number equals to the length of nums)

Traverse nums with two memories.

```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l = len(nums)
        mem = set()  # mem is to avoid repeated visit
        for i in range(l):
            if i in mem:
                continue
            seen = set()  # seen is to check if there is a loop
            direction = 1 if nums[i] > 0 else -1
            while True:
                if abs(nums[i]) == l or nums[i] % l == 0:  # loop to itself
                      break
                if i in seen:  # there is a loop
                    return True
                seen.add(i)
                mem.add(i)
                i = (i+nums[i]) % l  # next number
                if nums[i] * direction < 0:  # must be one direction
                    break
        return False
```
