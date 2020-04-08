## Approach

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

- My approach

My own brute force method was time limit exceeded.

- Other's approach

There is a very smart dynamic program method.

The key point is `second_buy` deducts the `first_profit`, so `second_profit` equals the sum of two transactions.

```python
class Solution(object):
    def maxProfit(self, prices):
        first_buy, second_buy, first_profit, second_profit = float('inf'), float('inf'), 0, 0
        for price in prices:
            first_buy = min(first_buy, price)
            first_profit = max(first_profit, price - first_buy)
            # Second_buy deducts first_profit, so the second contains informaiton both of first and second
            second_buy = min(second_buy, price - first_profit)
            second_profit = max(second_profit, price - second_buy)
        return second_profit
```
