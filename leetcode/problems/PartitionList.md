## Approach

[Problem link](https://leetcode.com/problems/partition-list/)

- My approach

Create two linked lists to store the less nodes and larger nodes, then link the large list at the end of less list.

```pyhon
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two linked lists
        less_head = le = ListNode(0)
        large_head = la = ListNode(0)
        n = head
        while n:
            if n.val < x:
                le.next = n
                le = le.next
            else:
                la.next = n
                la = la.next
            n = n.next
        la.next = None
        # Link the large list at the end of less list
        le.next = large_head.next
        return less_head.next
```
