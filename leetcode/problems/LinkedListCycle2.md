## Approach

[Problem link](https://leetcode.com/problems/linked-list-cycle-ii/)

- My approach

Use the same method as [Linked List Cycle](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/LinkedListCycle.md).

Traverse the linked list and create a set to save every node. And the first node which appears twice is the answer.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        mem = set()
        while head:
            mem.add(head)
            if head.next in mem:
                return head.next
            head = head.next
        return None
```

- Other's approach

This problem can also be solved by `O(1)` space complexity method.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # F, C. if they meet, F, 2F. 1st at 0, 2nd at F%C=h. C-h, h+2(C-h)=2C-h=C-h. 
        # (F+C-h) = k*C, F = (k-1)*C+h. means they will meet at the gate.
        # key point - O left, O up.
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # If the two pointers meet, set one of them to head and go on traverse
            # when they meet for the twice time, that node will be the answer
            if slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
```
