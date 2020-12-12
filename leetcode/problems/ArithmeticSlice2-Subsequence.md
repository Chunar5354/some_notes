## 446. Arithmetic Slices II - Subsequence

[Problem link](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)

- My approach

Use dynamic programming, and count[i][j] stands for the count of arithmetic elices end by i and their commom intervals are j.

For more explanations, see [official solution](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solution/).

```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = 0
        count = collections.defaultdict(dict)
        for i in range(len(A)):
            for j in range(i):
                interval = A[i] - A[j]
                _sum = 0
                if interval in count[j]:
                    _sum = count[j][interval]
                origin = 0
                if interval in count[i]:
                    origin = count[i][interval]
                count[i][interval] = origin + _sum + 1  # modify current count
                res += _sum
        return res
```
