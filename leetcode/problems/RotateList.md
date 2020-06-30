## Approach

[Problem link](https://leetcode.com/problems/rotate-list/)

- My approach

My idea is store the value of every node in a list, and rotate the list, finally transform the list into a linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        n = head
        # Save values into list
        nodes = []
        while n:
            nodes.append(n.val)
            n = n.next
        # For every multiple of len(nodes), the list rotate to the initial order,so we use a '%' to calculate the remainder
        num = k % len(nodes)
        # Rotate the list
        for i in range(num):
            crt_node = nodes.pop(-1)
            nodes.insert(0, crt_node)
        # Transform list into linked list
        new_head = nd = ListNode(nodes[0])
        for j in range(1, len(nodes)):
            nd.next = ListNode(nodes[j])
            nd = nd.next
        return new_head
```

And there is a method without using list.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        length = 0
        curr = head
        # Calculate length of linked list
        while curr:
            length += 1
            curr = curr.next
        # For every multiple of len(nodes), the list rotate to the initial order,so we use a '%' to calculate the remainder
        k %= length
        if k == 0:
            return head
        
        index = 0
        curr = head
        # After rotate k times, the new head is the (length-k+1)th node
        while index < length - k:
            curr = curr.next
            index += 1
        new_head = curr
        # And then add the nodes before new_head at end of new linked list
        while curr.next != new_head:
            if curr.next is None:
                curr.next = head
            curr = curr.next
        
        curr.next = None
        return new_head
```
