## Approach

[Problem link](https://leetcode.com/problems/binary-tree-postorder-traversal/)

- My approach

Iteratively do postorder traversal directly is complex. Because there need be a memory.

But since postorder is `left-right-root`, we can do a `root-right-left` traversal and resverse the result.

The `root-right-left` traversal is same like [Binary Tree Preorder Traversal](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BinaryTreePreorderTraversal.md).

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        n = root
        while stack or n:
            res.append(n.val)
            # Push left child into stack
            if n.left:
                stack.append(n.left)
            if n.right:
                n = n.right
            # If goes to the most right, pop from stack
            else:
                if not stack:
                    res.reverse()
                    return res
                else:
                    n = stack.pop()
        # Finally reverse the result
        res.reverse()
        return res
```
