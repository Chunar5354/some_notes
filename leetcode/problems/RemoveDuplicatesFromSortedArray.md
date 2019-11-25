## Solution

[Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

- My approach

It's an easy problem. Just remove the repeated elements of the array. But must modify the input array in-place.
So we can't simplily format it into a set.
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        i = 1
        n = nums[0]
        while i < len(nums):
            # If this element is equal to the last, pop current element
            if nums[i] == n:
                nums.pop(i)
            else:
                n = nums[i]
                i += 1
        return len(nums)
```

- Official approach

It uses two pointers, when find a different element, modify current position. It doesn't change the length of the array, just 
put all the different elements in the first n positions (n is the return value).
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            # When find a different element, modify current value
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1
```
