## 239. Sliding Window Maximum

[Problem link](https://leetcode.com/problems/sliding-window-maximum/)

- My approach

Move the window from left to right, if the new added element is larger than the previous maximum, modify the previous maximum. And if the element removed from window is the 
previous maximum, we need to recalculate the maximum.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        prev_max = max(nums[:k])
        res = [prev_max]
        for i in range(1, len(nums)-k+1):
            # If the max is removed
            if nums[i-1] == prev_max:
                prev_max = max(nums[i:i+k])
            # If the new element is larger than the max
            if nums[i+k-1] > prev_max:
                prev_max = nums[i+k-1]
            res.append(prev_max)
        return res
```

If we use the data structure `dqueue` in Python as the window, it can run faster.
