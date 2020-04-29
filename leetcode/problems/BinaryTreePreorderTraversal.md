## Approach

[Problem link](https://leetcode.com/problems/binary-tree-preorder-traversal/)

- My approach

By the topic requirements, need to solve this problem in iterative method.

The key point is to use `stack`, every time push the right child of current node into stack and when arrive at the most left node, pop 
from stack.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        n = root
        while stack or n:
            res.append(n.val)
            # Push righgt child into stack
            if n.right:
                stack.append(n.right)
            if n.left:
                n = n.left
            # If arrive the most left node, pop from stack
            else:
                if not stack:
                    return res
                n = stack.pop()
        return res
```

By the way, the problems like traverse a binary tree can be easily solved by recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(n):
            if not n:
                return
            res.append(n.val)
            helper(n.left)
            helper(n.right)
        helper(root)
        return res
```
