## Approach

[Problem link](https://leetcode.com/problems/search-insert-position/)

A very easy problem
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
```

Maybe you can try binary search method, but it's a little complex in code.
