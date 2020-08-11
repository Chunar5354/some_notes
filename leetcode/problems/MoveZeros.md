## 283. Move Zeroes

[Problem link](https://leetcode.com/problems/move-zeroes/)

- My approach

My idea is using two pointers. z stands for the index of 0, and p stands for the index of non-zero after z. Each time locating z and p, swap them.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        while z < len(nums) and nums[z] != 0:
            z += 1
        # p must after z 
        p = z
        while p < len(nums) and nums[p] == 0:
            p += 1
            
        while p < len(nums):
            if nums[p] != 0 and nums[z] == 0:
                nums[z], nums[p] = nums[p], nums[z]
            if nums[p] == 0:
                p += 1
            if nums[z] != 0:
                z += 1
```

- Official approach

The method of two pointers can be optimized.

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        z = 0
            
        while p < len(nums):
            if nums[p] != 0:
                nums[z], nums[p] = nums[p], nums[z]
                z += 1
            p += 1
```

Here z stands for the last non-zero number or the first 0. When p is a non-zero number, swap them.
