## 324. Wiggle Sort II

[Problem link](https://leetcode.com/problems/wiggle-sort-ii/)

- My approach

Firstly sort the array then divide the sorted array at the middle. Then add elements from small part and large part alternatelly.

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        small = nums[:(len(nums)+1)//2]
        large = nums[(len(nums)+1)//2:]

        while nums:
            nums.pop()
        while small:
            nums.append(small.pop())
            if large:
                nums.append(large.pop())
        if large:
            nums.append(large.pop())
```

- Other's approach

An O(1) space complex method.

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort() 
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
```
