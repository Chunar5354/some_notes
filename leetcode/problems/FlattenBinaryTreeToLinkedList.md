## Approach

[Problem link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

- My approach

Do a preorder traversal(can't be other orders) first and save the values into a list. Then update the tree by value list.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        val_list = []
        def helper(n):
            if not n:
                return
            val_list.append(n.val)
            helper(n.left)
            helper(n.right)
        # Preorder traverse
        helper(root)
        # Clear the left tree
        root.left = None
        node = root
        # Update the tree, only have right tree
        for val in val_list[1:]:
            crt_n = TreeNode(val)
            node.right = crt_n
            node = node.right
```

This method must traverse the tree two times, there is an one-time method.

- Other's approach

The key is every time link current right tree into the most right node of current left tree, then change left tree to right tree. 
After doing this, current left tree is cleared. And do same operation level by level.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        node = root
        while node:            
            if node.left:
                # Find the most right node of current left tree
                rightMostNode = node.left
                while rightMostNode.right:
                    rightMostNode = rightMostNode.right
                # Link the current right tree to most right node
                rightMostNode.right = node.right
                # Change left tree to right tree
                node.right = node.left
                # Clear left tree
                node.left = None
            # Go to next level
            node = node.right
```
