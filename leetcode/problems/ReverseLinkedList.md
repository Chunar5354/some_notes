## Approach

[Problem link](https://leetcode.com/problems/reverse-linked-list/)

- My approach

My idea is using array to save the nodes, and create a new linked list in reversed order.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        n = head
        # Save nodes into list
        n_list = []
        while n:
            n_list.append(ListNode(n.val))
            n = n.next
        # Create reversed linked list
        new_head = n_list.pop()
        n = new_head
        while n_list:
            n.next = n_list.pop()
            n = n.next
        return new_head
```

- Other's approach

There are two clear approaches.

1. Use two pointers.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        # Every time the order is: prev <- curr <- next_n
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        return prev
```

2. Recursing method

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(n):
            if not n or not n.next:
                return n
            # new_head is the reversed linked list until current node
            # for example, if current node is 3, new_head is 3<-4<-5
            new_head = helper(n.next)
            n.next.next = n
            n.next = None
            return new_head
        return helper(head)
```
