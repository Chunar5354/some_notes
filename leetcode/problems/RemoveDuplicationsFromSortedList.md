## Approach

[Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

- My approach

This problem is simplified [Remove Duplications From Sorted List 2](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/RemoveDuplicationsFromSortedList2.md)

Just traverse given list and remove duplications in-place.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        n = head
        while n:
            num = n.val
            # If there are duplications, skip them
            while n.next and n.next.val == num:
                n = n.next
            n = n.next
            head.next = n
            head = head.next
        return dummy.next
```
