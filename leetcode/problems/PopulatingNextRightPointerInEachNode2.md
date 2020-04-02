## Approach

[Problem link](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

- My approach

The same method of [Populating Next Right Pointer In Each Node](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/PopulatingNextRightPointerInEachNode.md) can solve this problem.

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
