## Approach

[Problem link](https://leetcode.com/problems/combination-sum-iii/)

- My approach

The key idea is using recursing to simplify the problem. 

For example, if the question is: `n=5, k=20`, we cando like this:

```
First time take one element [1], the question becomes [1] + answer of (n=4, k=19),
then take the second element(pay attention there can't be duplications), the question becomes [1, 2] + answer of (n=3, k=17).
Do this operation in cycle until finding all the answers.
```

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(curr):
            remain = n - sum(curr)
            # remain<0 means we add a large number, that can'e be the answer
            if remain < 0:
                return
            if remain == 0 and len(curr) == k:
                res.append(curr)
                return
            # To avoid duplications, each time we start with the last number plus 1
            for i in range(curr[-1]+1, 10):
                helper(curr + [i])
        
        for i in range(n-k):
            helper([i+1])
        return res
```
