## 442. Find All Duplicates in an Array

[Problem link](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

- My approach

Since all the numbers are larger than 1 and smaller than len(nums), we can use the numbers as index. 

For every number n, set nums[n] to negative, and when meet a number that its nums[n] is already negative, means this number has appeared before.

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                res.append(n)
            else:
                nums[n-1] *= -1
        return res
```
