## 430. Flatten a Multilevel Doubly Linked List

[Problem link](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

- My approach

Traverse the linked list and when meet a child node, add the child list between current node and current.next, use stack.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        n = head
        stack = []
        
        while n.next or stack or n.child:
            if not n.next:
                if stack:
                    curr = stack.pop()
                    if curr:
                        n.next = curr
                        curr.prev = n
            if n.child != None:
                stack.append(n.next)
                n.next = n.child
                n.child.prev = n
                n.child = None
            n = n.next
            if not n:
                break
        return head
```
