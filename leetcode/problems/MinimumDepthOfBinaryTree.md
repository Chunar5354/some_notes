## Approach

[Problem link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

- My approach

Check every node if both its left child and right child are None level by level.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        level = 1
        while stack:
            crt_stack = []
            for node in stack:
                # If current node doesn't have left child and right child, current level is the minimum level
                if not node.left and not node.right:
                    return level
                if node.left:
                    crt_stack.append(node.left)
                if node.right:
                    crt_stack.append(node.right)
            stack = crt_stack
            level += 1
        return level
```
