## 449. Serialize and Deserialize BST

[Problem link](https://leetcode.com/problems/serialize-and-deserialize-bst/)

- My approach

Use level traversal, ans when serialize the tree, use "X" to stand for None.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        stack = [root]
        res = ''
        while stack:
            curr_stack = []
            for n in stack:
                if not n:
                    res += 'X,'  # Use "," to sparate the values
                else:
                    res += str(n.val) + ','
                    curr_stack.append(n.left)
                    curr_stack.append(n.right)
            stack = curr_stack
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        stack = [root]
        i = 1
        while stack and i < len(data):
            curr_stack = []
            for n in stack:
                if data[i] != 'X':
                    n.left = TreeNode(int(data[i]))
                    curr_stack.append(n.left)
                i += 1
                if i >= len(data):
                    break
                if data[i] != 'X':
                    n.right = TreeNode(int(data[i]))
                    curr_stack.append(n.right)
                i += 1
                if i >= len(data):
                    break
            stack = curr_stack
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
```
