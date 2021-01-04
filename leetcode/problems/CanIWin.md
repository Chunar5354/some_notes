## 464. Can I Win

[Problem link](https://leetcode.com/problems/can-i-win/)

- Other approach

There is no simple ways, just enumerate all the possible conditions.

For a current number set basket, current player can win means the max number can exceed desiredTotal, or in the next round, the other player can't win.

Click [here](https://leetcode.com/problems/can-i-win/discuss/526008/dfs-%2B-memoization-%3A-easy-to-understand-with-explanation) to see more explanation.

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        basket = tuple(i+1 for i in range(maxChoosableInteger))
        
        if sum(basket) < desiredTotal:
            return False
        
        dic = {}  # set a memory to avoid duplications
        
        def dfs(basket,target):
            if basket[-1] >= target:  # current number is exceeded
                return True

            if basket in dic:
                return dic[basket]
            for i,num in enumerate(basket):
                if not dfs(basket[:i]+basket[i+1:],target-num):  # in the next round, the other player can't win
                    dic[basket] = True
                    return True
            dic[basket] = False
            return False
        return dfs(basket,desiredTotal)
```
