## Approach

[Problem link](https://leetcode.com/problems/maximum-gap/)

- My approach

Firstly sort the array and calculate all the different between adjacent numbers.

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        return res
```
