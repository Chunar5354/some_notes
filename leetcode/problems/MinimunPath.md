## Approach

[Problem link](https://leetcode.com/problems/minimum-path-sum/)

- My approach

This problem is also like [Unique Paths](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/UniquePaths.md).

And the magic is minimun length of current cell equals to the minimum of left and up cell plus current cell.
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # For the first column, the length of this cell is the sum of all the cells above
        for r in range(1, m):
            grid[r][0] = grid[r-1][0] + grid[r][0]
        # For the first row, the length of this cell is the sum of all the cells left
        for c in range(1, n):
            grid[0][c] = grid[0][c-1] + grid[0][c]
        # For every cell, the minimun length equals to the minimum of left and up cell plus current cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]

```
