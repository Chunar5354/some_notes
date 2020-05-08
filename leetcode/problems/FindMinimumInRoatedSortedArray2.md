## Approach

[Problem link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

- My approach

This problem is like [Find Munimum In Rotate Sorted Array](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/FindMunimumInRotateSortedArray.md).

And we can use the same code to solve it.

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]
```
