## 456. 132 Pattern

[Problem link](https://leetcode.com/problems/132-pattern/)

- Official approach

O(n) solution.

Firstly create an array minBefore that minBefore[i] stands for the minimum number befoer i.

Then traverse from right with stack, and we should keep the numbers in stack larger than minBefore[j], so if the number in stack is smaller than nums[j], we find a 132 patterm.

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minBefore = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            minBefore[i] = min(nums[i], minBefore[i-1])
        stack = []
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > minBefore[j]:
                while stack and stack[-1] <= minBefore[j]:  # delete the numbers smaller than the minimum of left
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
                
        return False
```
