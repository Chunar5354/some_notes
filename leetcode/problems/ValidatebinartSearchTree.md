## Approach

[Problem link](https://leetcode.com/problems/validate-binary-search-tree/)

- My approach

Binary Search Tree has a property that its inorder traverse is ascending.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        n_list = []
        n = root
        # Inorder traverse the binary tree 
        while stack or n:
            if n:
                stack.append(n)
            while n and n.left:        
                n = n.left
                stack.append(n)
            crt_n = stack.pop()
            n_list.append(crt_n.val)
            n = crt_n.right
        # Check if the list is in ascending order
        for i in range(1, len(n_list)):
            if n_list[i] <= n_list[i-1]:
                return False
        return True
```

And this method can be simplified.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        num = float('-inf')
        n = root
        while stack or n:
            while n:        
                stack.append(n)
                n = n.left
            crt_n = stack.pop()
            # Don't need to return a value list, just check during the traverse
            if crt_n.val <= num:
                return False
            num = crt_n.val
            n = crt_n.right
        return True
```

And this problem can also be solved by recursing method. Please see it at official solution.
