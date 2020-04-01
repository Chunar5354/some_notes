## Approach

[Problem link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

- My approach

Do level traverse, save the nodes in the same level from left to right, then link them.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = [root]
        while stack:
            crt_stack = []
            for i in range(len(stack)):
                # Save node into stack
                if stack[i].left:
                    crt_stack.append(stack[i].left)
                if stack[i].right:
                    crt_stack.append(stack[i].right)
                # Link nodes
                if i < len(stack)-1:
                    stack[i].next = stack[i+1]
            stack = crt_stack
        return root
```

And there is a method doesn't need to extra spaces to store nodes.

- Other's approach

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        original_root = root
        while root and root.left:
            current = root
            while current:
                # Link left child to right child
                current.left.next = current.right
                # Link current right child into the left child of next node
                if current.next:
                    current.right.next = current.next.left
                
                current = current.next
            # Every time go to the most left node of one level
            root = root.left
            
        return original_root
```
