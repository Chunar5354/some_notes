## Approach

[Problem link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

- My approach

This queestion is like [Binary Tree Level Order Traverse](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BinaryTreeLevelOrderTraverse.md). 
the only difference is the order of result.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        stack = [root]
        while stack:
            crt_value = []
            crt_stack = []
            for i in stack:
                if i.left:
                    crt_stack.append(i.left)
                    crt_value.append(i.left.val)
                if i.right:
                    crt_stack.append(i.right)
                    crt_value.append(i.right.val)
            stack = crt_stack
            if crt_value:
                res = [crt_value] + res
        return res
            
```
