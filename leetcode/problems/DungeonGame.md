## Approach

[Problem link](https://leetcode.com/problems/dungeon-game/)

- Other's approach

To solve this problem, we can do a dynamic program from end point to start point.

The key point is every position stands for `the least HP if the knight wants to get this position`.

```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 
        r = len(dungeon)
        c = len(dungeon[0])
        dp = [[0]*c for _ in range(r)]
        
        dp[-1][-1] = max(-dungeon[-1][-1]+1, 1)
        
        # If dp[i][j] is less than 0, means the HP has hurplus when get to current position, 
        # then we can set current position to 1, means the knight can get here with 1 HP
        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])
        
        for i in range(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1] - dungeon[-1][i])
            
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                dp[i][j] = max(1, min(dp[i][j+1],dp[i+1][j])-dungeon[i][j])
        
        return dp[0][0]
```
