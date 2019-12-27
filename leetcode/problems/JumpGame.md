## Approach

[Problem link](https://leetcode.com/problems/jump-game/)

- My approach

My idea is finding every 0 in nums, and check if the elements before 0 can jump over it. 
If can't jump over 0, means can't jump to the end.

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums or len(nums) <= 1:
            return True
        while 0 in nums:
            # Find current position of 0
            zero_position = nums.index(0)
            # If 0 is the last element, means can jum to 0
            if zero_position == len(nums) - 1:
                return True
            can_jump = False
            # Traverse elements before 0, if the value is larger than difference between two indexs,
            # means it can jump over this 0
            # Then set current 0 to -1, and go on finding next 0
            for i in range(zero_position):
                # Avoid -1 
                if nums[i] < 0:
                    continue
                if nums[i] > zero_position - i:
                    can_jump = True
                    break
            if not can_jump:
                return False
            nums[zero_position] = -1
        return True
```

- Official approach

There is a smart idea by official solution. Traverse from right to left, and reset the target element.
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        target = l - 1
        for i in range(l):
            current = l - i - 1
            # If can jump from current element to target, then current element can be the new target
            if nums[current] + current >= target:
                target = current
        # Finally check if the first element can be the target(can jump from first to last)
        return target == 0
```

For more details can read the official solution.
