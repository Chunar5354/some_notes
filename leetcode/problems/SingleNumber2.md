## Approach

[Problem link](https://leetcode.com/problems/single-number-ii/)

- My approach

Use the same mathod as [Single Number](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/SingleNumber.md).

Check is nums[i+1] == nums[i], if yes, means current number is not the single number, skip these three numbers.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            print(i)
            if nums[i] == nums[i+1]:
                i += 3
            else:
                return nums[i]
        return nums[-1]
```
