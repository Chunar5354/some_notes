## 297. Serialize and Deserialize Binary Tree

[Problem link](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

- My approach

My idea is serialize and deserialize the binary tree by using level order traversal.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        self.t = root
        s = []
        # Level order traversal
        stack = [root]
        while stack:
            temp = []
            for n in stack:
                if n != None:
                    s.append(str(n.val))
                    temp.append(n.left)
                    temp.append(n.right)
                else:
                    s.append('null')
            stack = temp
        
        # Remove all the null at the end
        i = len(s) - 1
        while s[i] == 'null':
            i -= 1
        res = '[' + ','.join(s[:i+1]) + ']'

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        l = data[1:-1].split(',')
        root = TreeNode(int(l[0]))
        # Reversed level order traversal
        stack = [root]
        i = 1
        while i < len(l):
            temp = []
            for n in stack:
                if not n:
                    continue
                if l[i] != 'null':
                    n.left = TreeNode(int(l[i]))
                else:
                    n.left = None
                i += 1
                if i >= len(l):
                    return root
                
                if l[i] != 'null':
                    n.right = TreeNode(int(l[i]))
                else:
                    n.right = None
                i += 1
                if i >= len(l):
                    return root
                
                temp.append(n.left)
                temp.append(n.right)
            stack = temp
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```
