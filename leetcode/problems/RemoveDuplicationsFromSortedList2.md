## Approach

[Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

- My approach

The idea is very simple: Traverse the sorted list from start to end, and delete the duplicated nodes.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = a = ListNode(0)
        num = head.val
        n = head.next
        # To end the loop, firstly add a flag at the end of given listnode
        while head.next:
            head = head.next
        head.next = ListNode('a')
        while n:
            # At the beginning of the loop, n stands for current node, num stands for the value of last node
            # If there are duplications, go on until next value
            if n.val == num:
                while n.val == num:
                    n = n.next
                num = n.val
                n = n.next
            # If there is no duplication, add ListNode(num) to the end of res
            else:
                a.next = ListNode(num)
                a = a.next
                num = n.val
                n = n.next
        return res.next
```

- Other's approach

There is an in-place method from others. The key idea is using two pointers.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        
        dummy = ListNode(0)
        # Set two pointers
        prev = dummy
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
        return dummy.next
```
