## Approach

[Problem link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

- My approach

Just improve the approach of [Binary Tree Level Order Traverse](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BinaryTreeLevelOrderTraverse.md), add a reverse to the 2n level.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        # Add a reverse
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res
```
