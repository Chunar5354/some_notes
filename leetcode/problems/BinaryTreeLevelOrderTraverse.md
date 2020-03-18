## Approach

[Problem link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- My approach

For each level, create a stack to store the nodes.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = [[root.val]]
        while stack:
            crt_stack = []
            crt_value = []
            # Save nodes into stack, and save values into value list
            for n in stack:
                if n.left:
                    crt_stack.append(n.left)
                    crt_value.append(n.left.val)
                if n.right:
                    crt_stack.append(n.right)
                    crt_value.append(n.right.val)
            stack = crt_stack
            if crt_value:
                res.append(crt_value)
        return res
```
