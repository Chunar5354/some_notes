## 334. Increasing Triplet Subsequence

[Problem link]https://leetcode.com/problems/increasing-triplet-subsequence/()

- My approach

Use two pointers to stands for the first number and the second number. When meet a number smaller then them, modify it, until finding the third number.

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        first = nums[0]
        second = float('inf')
        
        for n in nums:
            if n < first:
                first = n
            elif n > first and n < second:
                second = n
            # If find the third number, return true
            elif n > second:
                return True
        return False
```
