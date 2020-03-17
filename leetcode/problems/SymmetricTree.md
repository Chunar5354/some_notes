## Approach

[Problem link](https://leetcode.com/problems/symmetric-tree/)

- My approach

To check if a binary tree is a symmetric tree, we can divide the tree into left and right parts. For the left part, we always visit 
the left child first, and for right part, we always visit the right child first, and check if their values are the same.

Here is the recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse(left, right):
            if left == right == None:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            # Check the symmetric position
            return traverse(left.right, right.left) and traverse(left.left, right.right)
        if not root:
            return True
        return traverse(root.left, root.right)
```

And iterative method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # Set two stacks
        stack_left = [root.left]
        stack_right = [root.right]
        while stack_left and stack_right:
            new_left = []
            new_right = []
            while stack_left and stack_right:
                left = stack_left.pop()
                right = stack_right.pop()
                if left == right == None:
                    continue
                if not left or not right:
                    return False
                if left.val != right.val:
                    return False
                # For the left part, save the left child first, and save right child first for the right part
                new_left += [left.left, left.right]
                new_right += [right.right, right.left]
            stack_left = new_left
            stack_right = new_right
        return True
```
