## Approach

[Problem link](https://leetcode.com/problems/find-peak-element/)

- My approach

Traverse nums and find a element `nums[i]` that `nums[i] > nums[i+1]` and `nums[i] > nums[i-1]`.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[-1] > nums[-2]:
            return len(nums)-1
```

And there is a more improved `O(log(n))` method.

- Official approach

For more explanation, please see official solution.

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
```
