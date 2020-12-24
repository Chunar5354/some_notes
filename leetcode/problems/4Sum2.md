## 454. 4Sum II

[Problem link](https://leetcode.com/problems/4sum-ii/)

- Other's approach

Combinate two arrays as a group with the formate `{the_sum_of_two: count}`. Then calculate the four_sum by the two groups.

```python
from collections import defaultdict
class Solution: 
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB, CD = defaultdict(int), defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                AB[A[i] + B[j]] += 1
        
        for k in range(len(C)):
            for l in range(len(D)):
                CD[C[k] + D[l]] += 1
        
        total = 0
        for ab in AB:
            total += CD[-ab] * AB[ab]
        return total
```
