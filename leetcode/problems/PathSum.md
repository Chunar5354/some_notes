## Approach

[Problem link](https://leetcode.com/problems/path-sum/)

- My approach

Do a recursing traverse, sum all the values. And when get a leaf node, check if the sum of values equal to the given target.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
        def traceback(node, num):
            if not node:
                return False
            # If current node is a leaf node, check the sum
            if not node.left and not node.right:
                return num+node.val == _sum

            return traceback(node.left, num+node.val) or traceback(node.right, num+node.val)
        return traceback(root, 0)
```
