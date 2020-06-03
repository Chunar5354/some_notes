## Approach

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

- My approach

This problem is the extension of [Best Time To Buy And Sell Stock 3](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BestTimeToBuyAndSellStock3.md).

Because this problem need to sell k times, we can create a k time cycle.

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) == 0:
            return 0
        # If k is larger than half of the length of prices, the problem becomes the question `Best time to buy and sell stock 2`
        if k > len(prices) // 2:
            return sum((prices[i+1] - prices[i]) for i in range(len(prices) - 1) if prices[i+1] > prices[i])
        # Create two list to store buy prices and profit
        price_buy = [float('inf')]*k
        profit = [0]*k
        for p in prices:
            for i in range(k):
                # Current buy price is the minimum of itself and (current price - last profit)
                if i == 0:
                    price_buy[i] = min(price_buy[i], p)
                else:
                    price_buy[i] = min(price_buy[i], p-profit[i-1])
                # Current profit is the maximum of itself and (current price - current buy price)
                profit[i] = max(profit[i], p-price_buy[i])
        # Because every time the prices before current position is included in current buy prices(price_buy[i])
        # the final whole profit is profit[-1]
        return profit[-1]
```
