## 328. Odd Even Linked List

[Problem link](https://leetcode.com/problems/odd-even-linked-list/)

- My approach

Traverse the linked list and every time change the part before current node as an odd even linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = head
        while odd.next:
            odd = odd.next  # last odd node until current node
            if not odd.next:
                return head
            next_odd = odd.next.next
            temp = even.next
            
            even.next = odd.next  # last even node until current node
            even = even.next
            even.next = temp
            odd.next = next_odd
        return head
```
