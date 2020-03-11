## Approach

[Problem link](https://leetcode.com/problems/unique-binary-search-trees-ii/)

I was confused that BST(二叉搜索树) and BFS(广度优先搜索), so I did'nt understand this question firstly.

- Other's approach

The feature of BST is 'All the left children are smaller than current node, and all the right children are larger than current node'.

So we can do it by recursing method.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def genSubTree(elements: list):
            '''
            This function returns a list which can be all the available child tree of BTS,
            if it contains root, current res is the final result
            '''
            if len(elements) == 0:
                return [None]
            if len(elements) == 1:
                return [TreeNode(elements[0])]
            res = []
            for i in range(len(elements)):
                # The number smaller than current i is left child
                left = genSubTree(elements[:i])
                # The number larger than current i is right child
                right = genSubTree(elements[i+1:])
                for l in left:
                    for r in right:
                        root = TreeNode(elements[i])
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        if n == 0:
            return []
        return genSubTree(list(range(1, n+1)))
            
```

- Knowledge

BTS: Binary Search Tree, all the left children are smaller than current node, all the right children are larger than current node.

