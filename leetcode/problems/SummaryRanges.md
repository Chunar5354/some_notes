## 228.Summary Ranges

[Problem link](https://leetcode.com/problems/summary-ranges/)

- My approach

Traverse the array and compare nums[i] with nums[i-1], if their different is not 1, nums[i-1] will be the end of last string, and nums[i] will be the start of the next string.

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(-1)
        start = 0
        arrow = "->"
        res = []
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if start == i-1:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + arrow + str(nums[i-1]))
                start = i
        return res
```
