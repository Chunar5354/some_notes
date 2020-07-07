## Approach

[Problem link](https://leetcode.com/problems/maximal-square/)

- My approach

My idea is brute force. Traverse the matrix and check every element if they can make a square.

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        b = []
        for m in matrix:
            b += m
        if set(b) == {'0'}:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Check if a square can be constitued by current line matrix[top][left:right]
        def helper(top, left, right):
            for k in range(right-left-1):
                if top+k+1 >= m:
                    return 0
                if '0' in set(matrix[top+k+1][left:right]):
                    return 0
            return (right-left)**2
                
        res = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    right = j
                    # When finding a '1', find the most '1' on current row, this maybe the top edge of a square
                    while right < n and right-j < m-i and matrix[i][right] == '1':                      
                        right += 1
                        if right-j <= m-i:
                            curr_area = helper(i, j, right)
                        res = max(res, curr_area)
        
        return res
```

- Other's approach

The best method to solve this problem is dynamic programming.

There are two approached form official solution.

1.m*n dp

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        res = 0
        dp = []
        for i in range(m+1):
            dp.append([0]*(n+1))
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    # The key point is here
                    # Current element stands for the right-bottom corner of a square, and its value is the length of side
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        return res*res
```

2. n dp

We can set the dp from 2D to 1D. And make dp[i] stands for dp[i-1][j] in 2D, dp[i-1] stands for dp[i][j-1], and set a variable prev stands for dp[i-1][j-1].

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        res = 0
        prev = 0
        dp = [0]*(n+1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    # The principle is the same as 2D
                    dp[j] = min(prev, dp[j], dp[j-1]) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return res*res
```

For more explinations, please see [official solution](https://leetcode.com/problems/maximal-square/solution/)
