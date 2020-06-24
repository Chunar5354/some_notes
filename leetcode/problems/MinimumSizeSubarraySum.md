## Approach

[Problem link](https://leetcode.com/problems/minimum-size-subarray-sum/)

- My approach

My idea is using two pointers `start` and `end`, and compare the target number s and the sum of nums[start:end].

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        if max(nums) >= s:
            return 1
        res = len(nums)
        start = end = 0
        
        while end < len(nums)-1:
            # While the sum is smaller than s, extend end
            while end < len(nums)-1 and sum(nums[start:end+1]) <= s:
                end += 1
            # There is a available length now, save it
            if sum(nums[start:end]) >= s:
                res = min(res, end-start)
            # To find the minimum length, we need to shorten the left edge
            while sum(nums[start:end+1]) >= s:
                start += 1
            res = min(res, end-start+2)
        return res
```

The approach above can be improved, because every time calculate the sum will waste much time.

- Other's approach

The main idea is the same, but when shorten the left edge this approach reduces from the sum instead of calculating the sum every time, this can save time.

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        
        start = end = 0 
        temp_sum = 0
        res = len(nums)
        
        while end < len(nums):
            temp_sum += nums[end]
            end += 1
            while temp_sum >= s:
                res = min(end-start, res)
                # Reduce from sum
                temp_sum -= nums[start]
                start += 1
        
        return res
```
