## Approach

[Problem link](https://leetcode.com/problems/binary-tree-right-side-view/)

- My approach

Do a level order traversal, and add the last node into result.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # Do level order traversal
        while stack:
            # Add the most right node into result
            res.append(stack[-1].val)
            crt_stack = []
            for n in stack:
                if n.left:
                    crt_stack.append(n.left)
                if n.right:
                    crt_stack.append(n.right)
            stack = crt_stack
        return res
```
