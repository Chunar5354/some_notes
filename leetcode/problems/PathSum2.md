## Approach

[Problem link](https://leetcode.com/problems/path-sum-ii/)

- My approach

Use the same method as [Path Sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/PathSum.md), but add all values into a list.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> List[List[int]]:
        res = []
        def traceback(n, value_list):
            if not n:
                return
            if not n.left and not n.right:
                if n.val + sum(value_list) == _sum:
                    res.append(value_list+[n.val])
                return
            traceback(n.left, value_list+[n.val])
            traceback(n.right, value_list+[n.val])
        traceback(root, [])
        return res
```
