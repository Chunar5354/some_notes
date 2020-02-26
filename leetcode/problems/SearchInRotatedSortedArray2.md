## Approach

[Problem link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

- My approach

The given list is a sortd list, but cut off at a random position. So we can just compare the first and last number with target number. 
And then do the same thing as [Search in Rotated Sorted Array](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/SearchInRotatedSortedArray.md)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        # Check the first number
        if target >= nums[0]:
            for i in nums:
                if i == target:
                    return True
        else:
            # Check the last number
            if target <= nums[-1]:
                for j in range(len(nums)):
                    if nums[len(nums)-j-1] < target:
                        return False
                    if nums[len(nums)-j-1] == target:
                        return True
            else:
                return False
        return False
```
