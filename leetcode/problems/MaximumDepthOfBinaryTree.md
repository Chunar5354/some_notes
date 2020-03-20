## Approach

[Problem link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- My approach

A very easy question, use recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        def traceback(n, d):
            if not n:
                self.depth = max(self.depth, d)
                return
            traceback(n.left, d+1)
            traceback(n.right, d+1)
        traceback(root, 0)
        return self.depth
```
