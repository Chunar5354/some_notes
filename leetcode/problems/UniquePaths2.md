## Approach

[Problem link](https://leetcode.com/problems/unique-paths-ii/)

- My approach

Use the same method as [](), and set the number of obstacles to 0.
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # If the start cell or final cell is an obstacle, there is no way
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        # Set first column and row values to -1(because 1 stands for obstacles, we use negative number to count the ways), 
        # and when meet an obstacle, the cells after it will be set to 0,
        # because in the edge cells, if there is an obstacle before current cell, means this cell can't be arrivaled
        for k in range(m):
            if obstacleGrid[k][0] == 1:
                break
            obstacleGrid[k][0] = -1
        for l in range(n):
            if obstacleGrid[0][l] == 1:
                break
            obstacleGrid[0][l] = -1
        # For each cell, the ways equals to the sum of ways of left and up cell, and if left or cell is an obstacle, its way is 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                up = obstacleGrid[i-1][j]
                left = obstacleGrid[i][j-1]
                if up == 1:
                    up = 0
                if left == 1:
                    left = 0
                obstacleGrid[i][j] = left + up
        # Finally the answer is in obstacleGrid[m-1][n-1], but negative.
        return -obstacleGrid[m-1][n-1]
```
