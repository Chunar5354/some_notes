## Approach

[Problem link](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

- My approach

Use recursing method to traverse the tree in level order. And numbers in higher level have higher opsition.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node, rootVal):
            if not node:
                return
            # Root value has higher position
            crt_sum = rootVal*10+node.val
            if not node.left and not node.right:
                self.res += crt_sum
                return
            helper(node.left, crt_sum)
            helper(node.right, crt_sum)
        helper(root, 0)
        return self.res
```
