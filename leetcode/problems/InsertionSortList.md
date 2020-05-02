## Approach

[Problem link](https://leetcode.com/problems/insertion-sort-list/)

- My approach

Traverse the linked list, if the value of next node is smaller than current value, fetch the next node and traverse from head to find 
the insertion position.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # To simplify the procedure, add a dummy head to the linked list
        dummy = ListNode(float('-inf'))
        dummy.next = head
        crt_node = head
        while crt_node.next:
            if crt_node.val > crt_node.next.val:
                # Traverse from head
                new_head = dummy
                while new_head.next.val < crt_node.next.val:
                    new_head = new_head.next
                # Insert the node
                insert_node = crt_node.next
                crt_node.next = crt_node.next.next
                insert_node.next = new_head.next
                new_head.next = insert_node
            else:
                crt_node = crt_node.next
        return dummy.next
```
