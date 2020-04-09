## Approach

[Problem link](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

- My approach

Use recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def helper(node):
            if not node:
                return 0
            self.res = max(self.res, node.val)
            if not node.left and not node.right:
                return node.val
            # currentLeftsum: path sum of current left tree
            # currentRightsum: path sum of current right tree
            currentLeftSum = helper(node.left)
            currentRightSum = helper(node.right)
            # currentNodeSum: the maximum of left and right path sum plus current value, and return it to calculate higher level path sum
            currentNodeSum = max(currentLeftSum, currentRightSum, 0) + node.val
            # currentPathSum: if calculate stops at current node, current path sum will be (currentLeftSum + currentRightSum + node.val)
            currentPathSum = currentLeftSum + currentRightSum + node.val
            # Modify res to the maximum of these three values
            self.res = max(self.res, currentPathSum, currentNodeSum)
            return currentNodeSum
        helper(root)
        return self.res
```

- Explanation

For example, if the given binary tree is:
```
   -10
   / \
  9  20
    /  \
   15   7
```

When goes to node `20`, the variables will be:
```
currentLeftsum: 15
currentRightsum: 7
currentNodeSum: 35, which stands for: 
   20
  /  
 15
 currentPathSum: 42, which stands for:
    20
   /  \
  15   7
```

And when goes to node `-10`, the variables will be:
```
currentLeftsum: 9
currentRightsum: 42
currentNodeSum: 25, which stands for: 
   -10
     \
     20
    /  \
   15   7
 currentPathSum: 41, which stands for:
   -10
   / \
  9  20
    /  \
   15   7
```

So the maximum path sum is 42.
