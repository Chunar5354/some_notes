## Approach

[Problem link](https://leetcode.com/problems/binary-search-tree-iterator/)

- My approach

We can firstly do a preorder traversal, because preorder traversal of binary search tree is in ascending order.

And after getting the ascending order list, the next and hasNext operation is very easy.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        # Firstly do a preorder traversal to get a ascending order value list
        self.val = []
        def helper(n):
            if not n:
                return
            helper(n.left)
            self.val.append(n.val)
            helper(n.right)
        helper(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.val.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.val != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

But the method above has `O(n)` space complexity, not `O(h)`.

To have a `O(h)` space complexity, there is an official solution.

- Official approach

The key point is creating a stack to store left nodes, because in binary search tree, left node is smaller than root.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        # Stack for the recursion simulation
        self.stack = []
        
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
```

For explanation, please see official solution.
