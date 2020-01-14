## Approach

[Problem link](https://leetcode.com/problems/set-matrix-zeroes/)

- My approach

My idea is firstly traverse the matrix, find all the '0', save the positions into a list.
And then traverse the list, set every rows and columns to zero.
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        visited_row = []
        visited_column = []
        m = len(matrix)
        n = len(matrix[0])
        # Save all the positions into list zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for p in zeros:
            # Set the rows to 0, and save current row into memory
            if p[0] not in visited_row:
                matrix[p[0]] = [0] * n
                visited_row.append(p[0])
            # Set the columns to 0, and save current column into memory
            if p[1] not in visited_column:
                for l in range(m):
                    matrix[l][p[1]] = 0
                visited_column.append(p[1])
```

And there is an official with a similar idea, but a little faster.
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # Save the column and row in two different lists directly
        first_row = [1] * n
        first_column = [1] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    first_row[j] = 0
                    first_column[i] = 0
        for c in range(m):
            if first_column[c] == 0:
                matrix[c] = [0]*n
        for r in range(n):
            if first_row[r] == 0:
                for l in range(m):
                    matrix[l][r] = 0
```
