## Approach

[Problem link](https://leetcode.com/problems/house-robber-ii/)

- My approach

We can do [House Robber](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/HouseRobber.md) two times. To avoid circle, first time we don't rob the first house, 
and second time don't rob the last house.

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        # First rob
        prev_two = 0
        prev_one = 0
        res1 = 0
        for i in range(len(nums)-1):
            res1 = max(prev_one, prev_two+nums[i])
            prev_two = prev_one
            prev_one = res1
        
        # Second rob
        prev_two = 0
        prev_one = 0
        res2 = 0
        for i in range(1, len(nums)):
            res2 = max(prev_one, prev_two+nums[i])
            prev_two = prev_one
            prev_one = res2
        return max(res1, res2)
```
