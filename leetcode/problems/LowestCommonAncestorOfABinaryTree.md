## 236. Lowest Common Ancestor of a Binary Tree

[Problem link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

- My approach

This method is the extend of [Lowest Common Ancestor Of A Binary Search Tree](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/LowestCommonAncestorOfABinarySearchTree.md).

So my idea is creating a map of binary search tree for the given binary tree, by using inorder travsesal. And then find the lowest common ancestor in binart search tree.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.num = 0
        dic = {}
        # Do inorder traversal ans save the nodes as {value: index} in dictionary
        # The index is ascending as the traversal goes on
        def inorder(n):
            if not n:
                return
            inorder(n.left)
            dic[n.val] = self.num
            self.num += 1
            inorder(n.right)
        inorder(root)
        # Use the method of searching lowest common ancestor from a binary search tree
        min_target = min(dic[p.val], dic[q.val])
        max_target = max(dic[p.val], dic[q.val])
        n = root
        while n:
            if min_target > dic[n.val]:
                n = n.right
            elif max_target < dic[n.val]:
                n = n.left
            else:
                return n
```

But this is alittle complex. There is a smart method from official solution.

- Official solution

When traversing the tree, we return 1 if current node is one of thr target or current node is ancestor of current node, or return 0.

We can see that if current node is ancestor of the two targets, there must be at least two '1' in return. We can use this to solve the problem.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def helper(n):
            if not n:
                return 0
            left = helper(n.left)
            if n == p or n == q:
                curr = 1
            else:
                curr = 0
            right = helper(n.right)
            # If the sum of the three is equal or larger than 2, means current node is a ancestor
            # And as traversal goes down, the lower ancestor will override the higher ancestor
            if right + curr + left >= 2:
                self.res = n
                return 1
            return max(curr, left, right)
        helper(root)
        return self.res
```
