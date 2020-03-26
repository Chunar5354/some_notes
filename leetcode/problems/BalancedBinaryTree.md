## appeoach

[Problem link](https://leetcode.com/problems/balanced-binary-tree/)

- My approach

Check every node if its depth of left tree and right tree is balanced by recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def traceback(node, num):
            '''
            paras:
            :node: current node to check
            :num: a number from root to child(0 to n), level by level
            
            return: a list with two elements, the first is a bool object means if current node is balanced,
                    the second is a int object means the maximum number of left tree and right tree
            '''
            if not node:
                return (True, num)
            left = traceback(node.left, num+1)
            right = traceback(node.right, num+1)
            # Now the depth of left tree equals to (left - num), and also the right
            # Check if the differ of two depths is smaller than 1, and both left tree and right tree are balanced
            if abs(left[1]-right[1]) <= 1 and left[0] and right[0]:
                return (True, max(left[1], right[1]))
            else:
                return (False, max(left[1], right[1]))
        return traceback(root, 0)[0]
```
