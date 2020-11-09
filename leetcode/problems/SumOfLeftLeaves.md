## 404. Sum of Left Leaves

[Problem link](https://leetcode.com/problems/sum-of-left-leaves/)

- My approach

Recursing solution, and set a variable to check if current node is a left child.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        
        def helper(n, left):
            if not n:
                return
            if not n.left and not n.right:
                if left:
                    self.res += n.val
                return
            helper(n.left, True)
            helper(n.right, False)
        
        helper(root, False)
        return self.res
```

And local result version:

```python
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.recursive(root, 0, False)
        
        
    def recursive(self, root, sumi, isLeft):
        if not root:
            return sumi
        if isLeft and root and not root.left and not root.right:
            return sumi + root.val
        sumi = self.recursive(root.left, sumi, True)
        sumi = self.recursive(root.right, sumi, False)
        return sumi
```
