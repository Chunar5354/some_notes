## Approach

[Problem link](https://leetcode.com/problems/binary-tree-inorder-traversal/)

- My solution

Inorder traverse of binary tree(中序遍历), means for every node in binary tree, visit it as the order left child, self, right node.

We can use recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def traceback(n):
            if not n:
                return
            # If current node doesn't have left child, add current value into result, and traverse its right child
            if not n.left:
                self.res += [n.val]
                traceback(n.right)
            # The order: left child, self, right child
            else:
                traceback(n.left)
                self.res += [n.val]
                traceback(n.right)
                
        traceback(root)
        return self.res
```

And we can also use stack.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        n = root
        while n or stack:
            # Go left until there is no left child
            while n:
                stack.append(n)
                n = n.left
            n = stack.pop()
            res.append(n.val)
            n = n.right
        return res
```
