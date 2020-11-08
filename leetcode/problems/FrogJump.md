## 403. Frog Jump

[Problem link](https://leetcode.com/problems/frog-jump/)

- My approach

My own recursing solution was time limited exceeded.

- Other's approach

Use dynamic programming, save the structure as `{stone:(the steps taked to jump to this stone)}`.

Then traverse the given stones, for each stone, the next stone it can reach will be in `stone + (step-1, step, step+1)`.

After dealing with all the stones, if can jump to the final stone, there must be some values in the dic[final_stone].

```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = {i:set() for i in stones}
        dic[0] = {0}
        
        for stone in stones:
            for step in dic[stone]:
                for jump in (step-1, step, step+1):
                    nextStone = stone + jump  # The next stone can be reached
                    if nextStone != stone and nextStone in dic:
                        dic[nextStone].add(jump)
        
        return len(dic[stones[-1]]) > 0
```
