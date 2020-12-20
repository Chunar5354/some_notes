## 450. Delete Node in a BST

[Problem link](https://leetcode.com/problems/delete-node-in-a-bst/)

- My approach

For a binary search tree, when delete a node, means replace its value with its predecessor value(the most right node of left child), or the successor value(the most left node 
of right child). Go on do this replacement when get to leaf node, and just delete the leaf node.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key and not root.left and not root.right:
            return None
        n = root
        to_delete = n
        # Firstly find the node to delete
        while n.val != key:
            if n.val > key:
                if n.left and n.left.val == key:
                    to_delete = n.left
                    break
                n = n.left
            elif n.val < key:
                if n.right and n.right.val == key:
                    to_delete = n.right
                    break
                n = n.right
            if not n:
                return root
        
        def dele(to_delete, father):
            # for leaf nodes
            if not to_delete.left and not to_delete.right:
                if father.left and to_delete.val == father.left.val:
                    father.left = None
                else:
                    father.right = None
                return
            
            # Change the target node with the most left node of right child 
            # or most right node of left child
            # Then if the change node is not a leaf node, go on delete
            if not to_delete.left:
                to_change = to_delete.right
                father = to_delete
                while to_change.left:
                    father = to_change
                    to_change = to_change.left
                to_delete.val = to_change.val
                dele(to_change, father)
            else:
                to_change = to_delete.left
                father = to_delete
                while to_change.right:
                    father = to_change
                    to_change = to_change.right
                to_delete.val = to_change.val
                dele(to_change, father)
        
        dele(to_delete, n)
        return root
```
