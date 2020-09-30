## 363. Max Sum of Rectangle No Larger Than K

[Problem link](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

- My approach

My idea is saving the areas firstly, dp[i][j] stands for the area of square from dp[0][0] to dp[i][j]. Based on dp, we can search all the squares in the matrix.

```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = []
        for _ in range(m+1):
            dp.append([0]*(n+1))
        
        dp[1][1] = matrix[0][0]
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        
        res = float('-inf')
        for r in range(m+1):
            for c in range(n+1):
                for i in range(r+1, m+1):
                    for j in range(c+1, n+1):
                        # area from dp[r][c] to dp[i][j]
                        curr = dp[i][j] - dp[i][c] - dp[r][j] + dp[r][c]
                        if curr > k:
                            continue
                        elif curr == k:
                            return k
                        else:
                            res = max(curr, res)
        
        return res
```

This apporoach has O(m*m*n*n) time complex, and it was time limit exceeded.

- Other's approach

The approach above can be improved.

```python
class Solution:
    def maxSumSubmatrix(self, w: List[List[int]], K: int) -> int:
        
        def get(x1: int, y1: int, x2: int, y2: int) -> int:
            return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
        
        n, m = len(w), len(w[0])

        s = [[0 for i in range(m + 1)] for y in range(n + 1)]
        for i in range (1, n + 1):
            for j in range (1, m + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + w[i - 1][j - 1]
        
        res = -sys.maxsize
        for i in range(1, m + 1):
            for j in range(i, m + 1):
                L = [0]
                for k in range(1, n + 1):
                    si = get(1, i, k, j)
                    it = bisect.bisect_left(L, si - K)
                    if it != len(L):
                        res = max(res, si - L[it])
                    bisect.insort(L, si)
        return res
```

