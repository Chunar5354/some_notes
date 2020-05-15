## Approach

[Problem link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

- My approach

We can use the same method as [Two Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/TwoSum.md) to solve this problem.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(numbers):
            
            if target - val in d:
                return [d[target - val], idx+1]
            d[val] = idx+1
```

And since the given array is sorted, we can use such method:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
```
