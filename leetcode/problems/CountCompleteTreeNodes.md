## Approach

[Problem link](https://leetcode.com/problems/count-complete-tree-nodes/)

- My approach

My idea is doing level order traversal and record the levels.

Because only the last lavel may be uncomplete, the answer is the number of last level then plus 2^(level-1)-1.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        level = 0
        while stack:
            curr = []
            # The number of last level
            last_level = len(stack)
            for n in stack:
                if not n.left:
                    break
                curr.append(n.left)
                if not n.right:
                    break
                curr.append(n.right)
            stack = curr
            level += 1
        return 2**(level-1)-1+last_level
```

- Other's approach

This problem is better using recursing method.

Here is an example

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        l_level = 1
        l = root.left
        while l:
            l = l.left
            l_level+=1
        r_level = 1
        r = root.right
        while r:
            r = r.right
            r_level+=1
        # Only if current sub tree is a complete binary tree or a leaf node can return here
        if l_level == r_level:
            return int(math.pow(2,l_level)-1)
        
        # 1 stands for the root node, and number of all the nodes equals to root + left child + right child
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
```
