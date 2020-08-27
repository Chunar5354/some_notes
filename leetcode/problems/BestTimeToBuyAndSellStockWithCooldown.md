## 309. Best Time to Buy and Sell Stock with Cooldown

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

- My approach

My idea is using recursing method to enumerate all the possible situations, but it was time limited exceeded.

- Other's approach

There is a dynamic program from others.

The key point of dynamic program is finding the relationship of current element with the elements before.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# initialization
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)
```
