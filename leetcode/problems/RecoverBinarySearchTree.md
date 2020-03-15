## Approach

[Problem link](https://leetcode.com/problems/recover-binary-search-tree/)

- My approach

Firstlt I focus om how to change the two nodes, so I was confused and then searched for others' approach.

After seeing other's method, I realized that there is no need to change the two nodex, we just need to change the value of two nodes.

And there is a very smart method.

- Other's approach

He do an inorder traverse for the given binary tree. Save the nodes and values by order. And because the inorder traverse of a 
binary search tree is ascending, he sorts the value list, then recover the nodes.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        values = []
        self.inorder(root, nodes, values)
        # Sort the value list, and recover the binary tree
        values.sort()
        for i in range(len(nodes)):
            nodes[i].val = values[i]
        
    def inorder(self, root, nodes, values):
        '''
        inorder traverse the given tree, and save the value and nodes
        '''
        if root:
            self.inorder(root.left, nodes, values)
            nodes.append(root)
            values.append(root.val)
            self.inorder(root.right, nodes, values)
```

There is a method that don't need to recover all the nodes, just need to exchange the value of two wrong nodes.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        
        stack = []
        node = root
        previous = TreeNode(float('-inf'))
        # Do an inorder traverse
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # Inorder traverse of a binary sarch tree should be ascending
            # If current value is smaller than the previous one, previous node should be the wrong node
            # Then we just need to find the next wrong node, and exchange their values
            if previous.val > node.val:
                second = node
                if first is None:
                    first = previous
                else:
                    break
            previous = node
            node = node.right
        
        first.val, second.val = second.val, first.val
```
