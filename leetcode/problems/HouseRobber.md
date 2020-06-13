## Approach

[Problem link](https://leetcode.com/problems/house-robber/)

- My approach

My idea is using dynamic program, every time set current position to the result of nums[:i].

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        for i in range(2, len(nums)):
            # nums[i] equals to the result of nums[:i]
            nums[i] = max(nums[i-1], nums[i] + max(nums[:i-1]))
        return nums[-1]
```

There is a more easier method by using two pointers.

- Other's approach

The idea is the same, `curr` means the result of nums[:i], and `prev` means the retult of nums[:i-2].

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0, 0
        for n in nums:
            tmp = curr
            curr = max(prev + n, curr)
            prev = tmp
        return curr
```
