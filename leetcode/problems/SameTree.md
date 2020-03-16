## Approach

[Problem link](https://leetcode.com/problems/same-tree/)

- My approach

Traverse two trees and check if the two traverse list are the same.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            return not q
        if not q:
            return not p
        n_list = [p.val]
        def traverse(n):
            '''
            Traverse the tree by layer order, save the value (include null) into a list
            '''
            if n:
                if n.left:
                    n_list.append(n.left.val)
                else:
                    n_list.append(None)
                if n.right:
                    n_list.append(n.right.val)
                else:
                    n_list.append(None)
                traverse(n.left)
                traverse(n.right)
        traverse(p)
        p_list = n_list
        n_list = [q.val]
        traverse(q)
        return p_list == n_list
```

And there is a more easily method.

- Official approach

```python
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
```
