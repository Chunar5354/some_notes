## 235. Lowest Common Ancestor of a Binary Search Tree

[Problem link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- My approach

The common ancestor must meet the condition that `min target < current value < max target`.

So if `current value < min target`, the answer must be in the right child. And if `current value > max target`, the answer must be in left child. Or current node is the answer.

Here is the recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_node = min(p.val, q.val)
        max_node = max(p.val, q.val)
        def helper(node):
            if min_node > node.val:
                ans = helper(node.right)
            elif max_node < node.val:
                ans = helper(node.left)
            else:
                ans = node
            return ans
        return helper(root)
```

And the iterative.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_node = min(p.val, q.val)
        max_node = max(p.val, q.val)
        node = root
        while node:
            if min_node > node.val:
                node = node.right
            elif max_node < node.val:
                node = node.left
            else:
                return node

```
