## 257. Binary Tree Paths

[Problem link](https://leetcode.com/problems/binary-tree-paths/)

- My approach

Traverse the binary tree by recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        
        def helper(n, sub_res):
            if not n:
                return
            if not n.left and not n.right:
                res.append(sub_res + str(n.val))
            helper(n.left, sub_res + str(n.val) + '->')
            helper(n.right, sub_res + str(n.val) + '->')
        
        helper(root, '')
        return res
```
