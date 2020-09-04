## 322. Coin Change

[Problem link](https://leetcode.com/problems/coin-change/)

- My pproach

My recursing method was time limit exceeded.

- Official solution

The best way to solve this kind of greedy problem is dynamic program.

dp[x] stands for the minimum coins for x money.

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
```
