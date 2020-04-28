## Approach

[Problem link](https://leetcode.com/problems/reorder-list/)

- My approach

Save the nodes in a list and fetch nodes from right to leff, add them into linked list until middle node.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        n = head
        while n:
            nodes.append(n)
            n = n.next
        nodes = nodes[len(nodes)//2:]
        new_n = head
        while nodes:
            crt_node = nodes.pop()
            if new_n == crt_node:
                new_n.next = None
                return
            if new_n.next == crt_node:
                new_n.next.next = None
                return
            crt_node.next = new_n.next
            new_n.next = crt_node
            new_n = new_n.next.next
```

- Other approach

This problem can also be solved by `O(1)` method.

```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
```
