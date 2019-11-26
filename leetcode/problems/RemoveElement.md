## Solution

[Problem Link](https://leetcode.com/problems/remove-element/)

- My approach

It's also an easy problem. My idea is use `pop()` method.
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            # When find the val, pop it
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
```

But this approcah changed the whole length of nums.

There is an approach like [Remove Duplicates From Sorted Array](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/RemoveDuplicatesFromSortedArray.md)
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            # Put all elements that not val into front
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
```

And because we don't care the order of the return array, wo can also do like this:
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            # When find an element equal to val, put the last element into current position
            # and reduce the length number
            # It will return a reserve order
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
```
