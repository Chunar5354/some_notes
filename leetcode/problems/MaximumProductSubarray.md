## Approach

[Problem link](https://leetcode.com/problems/maximum-product-subarray/)

- My approach

We can solve this problem by dynamic program method. Make every element in nums equals to the product of all the elements before, 
expressed as `nums[i] = nums[0] * nums[1] * ... * nums[i]`. And finally answer is the maximum number in nums.

And there are two precautions:

  - 1.When meet a `0`, we need to skip it.
  - 2.Because there are negative numbers in nums, we need to multiply twice: from left to right and from right to left.
  

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new_nums = nums[::-1]
        # From left to right
        for i in range(1, len(nums)):
            # When meet 0, skip it
            if nums[i] == 0 or nums[i-1] == 0:
                continue
            nums[i] = nums[i] * nums[i-1]
        # From right to left
        for i in range(1, len(new_nums)):
            # When meet 0, skip it
            if new_nums[i] == 0 or new_nums[i-1] == 0:
                continue
            new_nums[i] = new_nums[i] * new_nums[i-1]
        return max(max(nums), max(new_nums))
```
