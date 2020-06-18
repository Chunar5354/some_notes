## Approach

[Problem link](https://leetcode.com/problems/remove-linked-list-elements/)

- My approach

Just traverse the linked list and remove the target nodes.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        # If the target value is at the head
        while head and head.val == val:
            head = head.next
        n = head
        while n and n.next:
            # Remove target nodes
            if n.next.val == val:
                n.next = n.next.next
            else:
                n = n.next
        return head
```
