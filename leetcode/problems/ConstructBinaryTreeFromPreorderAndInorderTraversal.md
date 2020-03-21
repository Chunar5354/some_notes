## Approach

[Problem link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

- My approach

My idea is check the index of preorder in inorder, if current index is smaller than the value of current node, it will be the left child, 
otherwise it will be the right child.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            n = root
            # Every time start check from the root
            while True:
                if inorder.index(preorder[i]) < inorder.index(n.val):
                    if not n.left:
                        n.left = TreeNode(preorder[i])
                        break
                    else:
                        n = n.left
                if inorder.index(preorder[i]) > inorder.index(n.val):
                    if not n.right:
                        n.right = TreeNode(preorder[i])
                        break
                    else:
                        n = n.right
        return root
```

But because this method must start the check from root every time, it's time limit exceeded.

- Other's approach

Then I found an other's recursing method, he uses both the property of preorder and inorder traversal.

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
		
        index_map = {}
        for indx, val in enumerate(inorder):
            index_map[val] = indx
        
        def helper(in_left=0, in_right=len(inorder)):
            # Use the index of inorder to stop recursing
            if in_left == in_right:
                return None

            rootval = preorder.pop(0)
            index = index_map[rootval]

            root = TreeNode(rootval)
            root.left = helper(in_left, index)
            # Because the order of preorder traversal is root-left-right, so after dealing with all the nodes of left tree,
            # preorder list will pop all the values of left tree, the new preorder[0] now is the root of right tree.
            root.right = helper(index+1, in_right)
        
            return root
        
        
        return helper()
```
