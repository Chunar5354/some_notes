## Approach

[Problem link](https://leetcode.com/problems/number-of-islands/)

- My approach

Traverse the grid and when meet a '1', update all the connected '1' to 'X'. So every '1' stands for a new island.

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        m = len(grid)
        n = len(grid[0])
        
        def helper(r, c):
            '''
            Update all the connected '1' to 'X'
            '''
            grid[r][c] = 'X'
            if r-1 >= 0 and grid[r-1][c] == '1':
                helper(r-1, c)
            if c-1 >= 0 and grid[r][c-1] == '1':
                helper(r, c-1)
            if r+1 <= m-1 and grid[r+1][c] == '1':
                helper(r+1, c)
            if c+1 <= n-1 and grid[r][c+1] == '1':
                helper(r, c+1)
                
        for i in range(m):
            for j in range(n):
                # Because connected '1' are now 'X', every new '1' means there is a new island
                if grid[i][j] == '1':
                    island += 1
                    helper(i, j)
        return island
```
