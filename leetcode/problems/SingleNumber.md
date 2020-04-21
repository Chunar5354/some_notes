## Approach

[Problem link](https://leetcode.com/problems/single-number/)

- My solution

FIrstly sort the array, and check if nums[i+1] = nums[i]

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            # If current number is not single, skip two same numbers
            if nums[i+1] == nums[i]:
                i += 2
            else:
                return nums[i]
        return nums[-1]
```

- Official solution

This problem is very suitable to use `XOR` method.

Because `a⊕b⊕a=(a⊕a)⊕b=0⊕b=b`

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```
