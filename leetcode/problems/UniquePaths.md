## Approach

[Problem link](https://leetcode.com/problems/unique-paths/)

- My solution

My idea is using recursing method, but it's time ecdeeded.

Then I found an other's method using a m*n matrix, very smart.

- Other's solution

The magic is the number of ways of current point equals to the ways of the sum its `left and up` point.

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Set a m*n matrix
        mat =[[0 for i in range(m)] for j in range(n)]
        # The up and left edge points only have one way directed to them
        for j in range(m):
            mat[0][j]=1
        for i in range(n):
            mat[i][0]=1
        # For every other point, ways to them equals to sum of ways of their left and up points
        for i in range(1,n):
            for j in range(1,m):
                mat[i][j]=mat[i][j-1]+mat[i-1][j]
        # And finally, the number of ways to the end is in mat[m-1][n-1]
        return mat[n-1][m-1]
```
