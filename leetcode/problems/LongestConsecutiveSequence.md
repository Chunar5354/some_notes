## Approach

[Problem link](https://leetcode.com/problems/longest-consecutive-sequence/)

- My approach

Sort the array first then traverse.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        start = nums[0]
        res = 0
        for i in range(1, len(nums)):
            # Skip the same numbers
            if nums[i] == nums[i-1]:
                continue
            # If the sequence is breaked, calculate the length and modify start number
            if nums[i] - nums[i-1] != 1:
                res = max(res, nums[i-1]-start+1)             
                start = nums[i]
        return max(res, nums[i]-start+1)
```
