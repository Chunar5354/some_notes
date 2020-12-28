## 458. Poor Pigs

[Problem link](https://leetcode.com/problems/poor-pigs/)

- Other's approach

Use mathematical method, see the number of pigs as bit, and test time as group. The buskets should less than `(times+1)^pigs`.

For more explanation, please see [here](https://leetcode.com/problems/poor-pigs/discuss/935112/Python-Math-solution-detailed-expanations).

```python
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        return ceil(log(buckets)/log(minutesToTest//minutesToDie + 1))
        # use swap formula : loga(b) = logc(b)/logc(a)
```
