## Approach

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

- My approach

Firstly I did a brout force method.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            # Maximum of the rest subtract current number
            res = max(res, max(prices[i+1:])-prices[i])
        return res
```

But it runs very slowly, so I did a new one-pass method.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            # Make prices[i-1] always be the minimum number in prices[:i]
            if prices[i] > prices[i-1]:
                res = max(res, prices[i]-prices[i-1])
                prices[i] = prices[i-1]
        return res
```
