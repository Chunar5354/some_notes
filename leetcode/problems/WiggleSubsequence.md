## 376. Wiggle Subsequence

[Problem link](https://leetcode.com/problems/wiggle-subsequence/)

- My approach

Dynamic programming with O(n^2) time complexity.

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 1
        # delete adjacent numbers
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        if len(nums) <= 1:
            return len(nums)
            
        diff = [0] * (len(nums)-1)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] > 0:
                diff[i] = 1
            elif nums[i+1]-nums[i] < 0:
                diff[i] = -1
        
        length = [1] * len(diff)
        for i in range(1, len(diff)):
            for j in range(i):
                if diff[i]*diff[j] == -1:
                    length[i] = max(length[i], length[j]+1)
                    
        return max(length) + 1
```

- Other's approach

Use two variables to store the up sequence and down sequence.

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                up = down + 1
            elif nums[i] - nums[i-1] < 0:
                down = up + 1
        return max(up, down)
```


