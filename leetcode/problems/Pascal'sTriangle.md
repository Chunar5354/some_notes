## Approach

[Problem link](https://leetcode.com/problems/pascals-triangle/)

- My approach

Use dynamic program, create a triangle and populate it level by level.

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        for j in range(2, len(res)):
            for k in range(1, len(res[j])-1):
                res[j][k] = res[j-1][k-1] + res[j-1][k]
        return res
```
