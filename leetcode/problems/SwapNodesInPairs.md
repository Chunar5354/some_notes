## Solution

[Problem Link](https://leetcode.com/problems/swap-nodes-in-pairs/)

- My solution

This problem is not very difficult, it's just about delete and insert operation of linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = a = ListNode(0)
        h.next = a.next = head
        while a.next:
            # To swap two nodes, firstly create two pointers of them: fir and sec
            fir = a.next
            sec = fir.next
            # If sec is None, means there is a single node at the end, just return
            if not sec:
                return h.next
            fir.next = sec.next
            sec.next = fir
            # After swapping them, we should connect the list together again
            a.next = sec
            a = fir
        return h.next
```

The other approches are the same as mine.
