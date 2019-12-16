## Approach

[Problem link](https://leetcode.com/problems/jump-game-ii/)

- My approach

The key of this problem is find the max of `value + index`, it means the longest step to jump.
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        final = len(nums) - 1
        jump_times = 0
        while i < len(nums) - 1:
            jump_times += 1
            # Calculate the distance from current element to the last element
            dis = final - i
            # If the distance is smaller than current number, means we can jump to the last element from current element
            if dis <= nums[i]:
                return jump_times
            else:
                step_d = {}
                # If distance is larger than current number, 
                # we search in the next 'n' elements in nums, which 'n' equals to current number
                # (because from current number, we can jump to 'n' steps),
                # if there is a element which value is larger than distance, means we can jump to the final from this number
                sub_n = nums[i+1: i+nums[i]+1]
                for j in range(len(sub_n)):
                    if sub_n[j] >= dis:
                        return jump_times + 1
                    else:
                        step_d[sub_n[j]+j] = j
                # If there is no element larger than distance, we find the number which the value of (sub_n[j]+j) is the largest,
                # and it is the next jump-to element, then go on
                next_step = step_d[max(step_d.keys())]
                i += next_step+1
        return jump_times + 1
```

And there is a more concise way by others
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        tmp = [i + v for i, v in enumerate(nums)]
        left = right = res = 0
        while right < len(nums)-1:
            # Fucking 'max(tmp[left:right+1])'
            left, right, res = right, max(tmp[left:right+1]), res + 1
        return res
```
