## 462. Minimum Moves to Equal Array Elements II

[Problem link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

- My approach

The final number of the minimum move is the median number of nums. So the result is the sum of distances to median number.

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        m = l // 2
        if l % 2 == 0:
            median = (nums[m]+nums[m-1]) // 2
        else:
            median = nums[m]
        res = 0
        for n in nums:
            res += abs(n-median)
        return res
```
