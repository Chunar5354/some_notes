## Approach

[Problem link](https://leetcode.com/problems/spiral-matrix/)

- My approach

Something like force approach. Divide the sprial into four directions: right, down, left, up.
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        end = n // 2
        l = 0
        res = []
        # When arrive half of rows, the sprial is over
        while l <= end:
            # right
            r = l - 1   # The start of right direction
            if r < 0:
                r = 0
            while r < n-l:
                res.append(matrix[l][r])
                r += 1
            # To avoid duplications, at end of every direction, we should judge if all the elements in matrix
            # have been in res
            if len(res) == m*n:
                return res
            # down
            d = l + 1   # The start of down direction
            while d < m-l:
                res.append(matrix[d][r-1])
                d += 1
            if len(res) == m*n:
                return res
            # left
            left = n - l - 2    # The start of left direction
            while left >= l:
                res.append(matrix[d-1][left])
                left -= 1
            if len(res) == m*n:
                return res
            # up
            u = m - l - 2    # The start of up direction
            while u > l+1:
                res.append(matrix[u][left+1])
                u -= 1
            if len(res) == m*n:
                return res
            l += 1
        return res
```

- Offical approach

In offical approach, there is a good idea of setting directions in list.
```python
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        # For rows, firstly on the right direction, the index of row doesn't change
        # secondly on the down direction, the index of row will plus 1 every time
        # thirdly on the left direction, the index of row doesn't change
        # finally on the up direction, the index of row will reduce 1 every time
        dr = [0, 1, 0, -1]
        # And for columns there is also a rule
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                # If conditions are not met, change next direction
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```

And there is also an approach using recursing method, but it's a little complex. If you want to see the details, please go to the 
official page.
