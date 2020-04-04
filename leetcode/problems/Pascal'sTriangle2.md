## Approach

[Problem link](https://leetcode.com/problems/pascals-triangle-ii/)

- Ny approach

Use same method like [Pascal's Triangle](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/Pascal'sTriangle.md), and return the last element instead.

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]*(i+1) for i in range(rowIndex+1)]
        for j in range(2, len(res)):
            for k in range(1, len(res[j])-1):
                res[j][k] = res[j-1][k-1] + res[j-1][k]
        return res[-1]
```
