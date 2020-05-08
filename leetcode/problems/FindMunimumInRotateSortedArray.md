## Approach

[Problem link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

- My approach

This is an easy problem. Just traverse nums, if current number is smaller than the number before, current number is the answer. 
If there is no such a number(means the given array is sorted), the first number nums[0] is the minimum number.

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]
```

