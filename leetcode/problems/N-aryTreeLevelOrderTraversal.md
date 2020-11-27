## 429. N-ary Tree Level Order Traversal

[Problem link](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

- My approach

Use stack.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            sub_stack = []
            sub_res = []
            while stack:
                curr = stack.pop(0)
                sub_res.append(curr.val)
                sub_stack += curr.children
            stack = sub_stack
            res.append(sub_res)
        
        return res
```
