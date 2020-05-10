## Approach

[Problem link](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Problem 156-159 are locked, so here start at 160.

- My approach

Save the nodes of linked list A into a set, and traverse linked list B until there is a node in the set(A).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lA = set()
        while headA:
            lA.add(headA)
            headA = headA.next
        while headB:
            if headB in lA:
                return headB
            headB = headB.next
        return None
```
