## 448. Find All Numbers Disappeared in an Array

[Problem link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

- My approach

1. Since 1 <= nums[i] <= n, we can modify nums with nums[i] as their indexes. For every n in nums, mutiply -1 if nums[n] is positive, finally the positions with positive numbers 
are the missing numbers.

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        for n in nums:
            n = abs(n)
            if nums[n] > 0:
                nums[n] *= (-1)
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i)
        return res
```

2. Use set

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        whole = set(range(1, len(nums)+1))
        n = set(nums)
        return list(whole-n)
```
