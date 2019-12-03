## Approach

[Problem link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

- My approach

This is also a problem asks to be solved by 'O log(n)` runtime complexity.

So use dichotomy(or binary search) method.
```python
class Solution:
    # When in main function find an element == target, 
    # use this function to find the result interval
    def findResult(self, nums, index, target):
        lt = rt = index
        while lt >= 0 and nums[lt] == target:
            lt -= 1
        while rt <= len(nums)-1 and nums[rt] == target:
                rt += 1
        return [lt+1, rt-1]
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        if l == r:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        while l < r:
            # If target > max or target < min, means target is not in nums
            if target > nums[r] or target < nums[l]:
                return [-1, -1]
            # If nums[l] or nums[r] or nums[mid] == target, call findResult() to get the answer
            if nums[l] == target:
                res = self.findResult(nums, l, target)
                return res
            if nums[r] == target:
                res = self.findResult(nums, r, target)
                return res
            mid = (l + r) // 2
            if nums[mid] == target:
                res = self.findResult(nums, mid, target)
                return res
            # Update left and right
            elif nums[mid] > target >= nums[l]:
                r = mid - 1
            elif nums[mid] < target <= nums[r]:
                l = mid + 1

        return [-1, -1]   
```

This approach is a little complex, it doesn't avoid come special situations such as `nums=[]`.

- Offical approach

Offical approach also uses binary search, but there is a magic logic, you should go to the page to see 
the [picture demonstrate](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/) to understand better.

```python
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        # If left is True, means finding the left edge,
        # is left is False, means finding the right edge
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        
        # Why this can avoid the special situations??
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
```
