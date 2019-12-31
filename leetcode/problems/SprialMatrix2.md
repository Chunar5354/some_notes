## Approach

[Problem link](https://leetcode.com/problems/spiral-matrix-ii/)

- My approach

We can use the same method as [Sprial Matirx](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/SprialMatirx.md).
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = []
        res = []
        for i in range(n):
            res.append([0]*n)
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = index = 0
        for i in range(1, n**2+1):
            res[r][c] = i
            visited.append((r, c))
            # Set two intermediate variables then judge them
            cr = r + dr[index]
            cc = c + dc[index]
            # If intermediate variables are available, ser (r, c) = (cr, cc)
            if (cr, cc) not in visited and 0 <= cc < n and 0 <= cr < n:
                r = cr
                c = cc
            # If they are not available, change the direction
            else:
                index = (index + 1) % 4
                r += dr[index]
                c += dc[index]
        return res
```
