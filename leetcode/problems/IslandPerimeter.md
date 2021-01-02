## 463. Island Perimeter

[Problem link](https://leetcode.com/problems/island-perimeter/)

- My approach

Every cell has 4 perimeters, but if one cell is connected with another cell, the count of perimeters will be reduced by 2.

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i-1 >= 0 and grid[i-1][j] == 1) and (j-1 >= 0 and grid[i][j-1] == 1):
                        continue
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        count += 2
                    elif j-1 >= 0 and grid[i][j-1] == 1:
                        count += 2
                    else:
                        count += 4
        return count
```
