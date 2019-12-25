## Approach

[Problem link](https://leetcode.com/problems/maximum-subarray/)

- My approach

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        current_sum = 0
        for i in range(len(nums)):
            # Add numbers from left to right
            current_sum += nums[i]
            if current_sum > 0:
                res = max(res, current_sum)
            # When current_sum < 0, means the sum of left part is negative,
            # and if go on adding, the left part will reduce the whole sum,
            # so we should abandon the left part by reset current_sum to 0
            else:
                current_sum = 0
        
        max_nums = max(nums)
        if max_nums <= 0:
            return max_nums
        return max(res, max_nums)
```

But I didn't find the approach of `divide and conquer` mentioned by the question.
