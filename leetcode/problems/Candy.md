## Approach

[Problem link](https://leetcode.com/problems/candy/)

- My approach

Traverse from left to right, if current rating value is larger than the last one, current child will get more candies than last 
child(c[i-1]+1). Then traverse from right to left, do the same operation.

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        c = [1] * len(ratings)
        # From left to right
        for i in range(1, len(c)):
            if ratings[i] > ratings[i-1] and c[i] <= c[i-1]:
                c[i] = c[i-1] +1
        # From right to left
        for i in range(len(c)-2, -1, -1):
            if ratings[i] > ratings[i+1] and c[i] <= c[i+1]:
                c[i] = c[i+1] + 1
        return sum(c)
```

In `official solution`, there is a `O(n)` method, but it's a little complex. For more information please view official solution.
