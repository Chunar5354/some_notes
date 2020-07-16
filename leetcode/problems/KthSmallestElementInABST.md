## 230. Kth Smallest Element in a BST

[Problem link](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

- My approach

If we do inorder traversal for a binary search tree, the nodes will be in ascending order. So we do it using recursing method, and the kth node will be the answer.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.t = 0
        self.res = 0
        self.get_res = False
        def helper(n):
            if self.get_res:
                return
            if not n:
                return
            if not n.left and not n.right:
                self.t += 1
                if self.t == k:
                    self.res = n.val
                    self.get_res = True
                return
            # Left child
            helper(n.left)
            # Current root
            self.t += 1
            if self.t == k:
                self.res = n.val
                self.get_res = True
                return
            # Right child
            helper(n.right)
        helper(root)
        return self.res        
```

ANd this method can get the O(1) space complex.
