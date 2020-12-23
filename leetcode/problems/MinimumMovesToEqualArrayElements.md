## 453. Minimum Moves to Equal Array Elements

[Problem link](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

- My approach

Mathimatical method.

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-min(nums)*len(nums)
```
