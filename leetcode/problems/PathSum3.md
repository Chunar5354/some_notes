## 437. Path Sum III

[Problem link](https://leetcode.com/problems/path-sum-iii/)

- My approach

Traverse the tree and for every node, traverse it with all the possible sums. For example, the possible sum of left child can be `[left.val, root.val]`.

```python
class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> int:
        self.res = 0
        def helper(n, untilNow):  # untilNow stores all the possible sums for current node
            if not n:
                return
            if n.val == _sum:
                self.res += 1
            for i in range(len(untilNow)):
                untilNow[i] += n.val
                if untilNow[i] == _sum:
                    self.res += 1
            helper(n.left, [n.val]+untilNow)
            helper(n.right, [n.val]+untilNow)
            
        helper(root, [])
        return self.res
```

Other's approach

Traverse with cache, where cache records the length of `current sum + target sum`, so during traversing the child tree of current node, when meet a node that its sum equals to 
one record in cache, means that the sum `from the record node to that child node` equals to target sum.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> int:
        
        def helper(n, untilNow):
            if not n:
                return
            untilNow += n.val
            self.res += self.d[untilNow]
            self.d[untilNow+_sum] += 1
            # let current node be 'cn', if meet a child node that its untilNow=(current until+_sum), 
            # means the path from cn to the child node equals to _sum
            helper(n.left, untilNow)
            helper(n.right, untilNow)
            self.d[untilNow+_sum] -= 1
        
        self.res, self.d = 0, collections.defaultdict(int)
        self.d[_sum] = 1
        helper(root, 0)
        return self.res
```
