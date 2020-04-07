## Approach

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

- My approach

Use the similar method like [Best Time To Buy And Sell Stock](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BestTimeToBuyAndSellStock.md)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        crt_buy = prices[0]
        for i in range(1, len(prices)):
            # If current price is larger than crt_buy, current profit equals prices[i]-crt_buy, add it to res,
            # and then the last but price(crt_buy) can't be used twice, modify crt_buy to prices[i]
            if prices[i] > crt_buy:
                res += (prices[i]-crt_buy)
                crt_buy = prices[i]
            # If current price is smaller than brt_buy, means if we buy at current price can get larger profit, 
            # so modify crt_buy to prices[i]
            else:
                crt_buy = prices[i]
        return res
```
