## Approach

[Problem link](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- My approach

This question is like [Construct Binary Tree From Preorder And Inorder Traversal](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/ConstructBinaryTreeFromPreorderAndInorderTraversal.md), 
but the order changes from inorder(root-left-right) to postorder(left-right-root). We can use the same method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def traceback(left, right):
            if left > right:
                return None
            # Pop postorder from right to left, the order means root-right-left
            num = postorder.pop()
            root = TreeNode(num)
            idx = inorder.index(num)
            root.right = traceback(idx+1, right)
            # After dealing with the right tree, current postorder[-1] should be the root of left tree
            root.left = traceback(left, idx-1)
            return root
        return traceback(0, len(inorder)-1)
```

And this method can be improved by using dictionary.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        dic = {}
        # Use dictionary to save the index od values in inorder list
        for indx, val in enumerate(inorder):
            dic[val] = indx
        def traceback(left, right):
            if left > right:
                return None
            num = postorder.pop()
            root = TreeNode(num)
            # Get data by key-value method can run faster than index() method
            idx = dic[num]
            root.right = traceback(idx+1, right)
            root.left = traceback(left, idx-1)
            return root
        return traceback(0, len(inorder)-1)
```
