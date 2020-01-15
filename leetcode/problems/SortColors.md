## Approach

[Problem link](https://leetcode.com/problems/sort-colors/)

- My approach

By the prompt of the qiestion, I traverse the given list and record the count of '0', '1' and '2'. Then reset 'nums' by them.

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = b = 0
        # Record the counts
        for i in nums:
            if i == 0:
                r += 1
            if i == 1:
                w += 1
            if i == 2:
                b += 1
        # Reset nums
        for j in range(r):
            nums[j] = 0
        for k in range(r, r+w):
            nums[k] = 1
        for l in range(r+w, r+w+b):
            nums[l] = 2
```

This approach uses a two-pass algorithm, and there is a smart one-pass algorithm.
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use three pointers
        left, right, cur = 0, len(nums) - 1, 0
        while cur <= right:
            # If meet a '0', change current pointer and the left pointer, and add each of them
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur, left = cur + 1, left + 1
            # If meet a '2', change current pointer and right pointer, and reduce only right pointer
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right = right - 1
            # If meet a '1', just add current pointer
            else:
                cur += 1
```

