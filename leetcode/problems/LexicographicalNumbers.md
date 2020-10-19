## 386. Lexicographical Numbers

[Problem link](https://leetcode.com/problems/lexicographical-numbers/)

- My approach

Think the numbers as a tree, which the children are based on the root, like this:

```
   1       2           9
 /   \   /  \         /  \
10...19 20...29 ...  90...99
```

We do `DFS` of these trees from left to right, the order will be lexicographical order.

```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.res = []
        def helper(curr):
            if curr > n:
                return
            self.res.append(curr)
            for i in range(10):
                if curr*10+i > n:
                    return
                helper(curr*10+i)  # dfs
                
        for i in range(1, 10):
            helper(i)
        return self.res
```
