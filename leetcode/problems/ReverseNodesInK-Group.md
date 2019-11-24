## Solution

[Problem Link](https://leetcode.com/problems/reverse-nodes-in-k-group/)

- My solution

My idea is to store the linked list into a python list, and use the `list.reverse()` method.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        res = []
        # Every time reverse the first k elements in l, then add into res
        while len(l) >= k:
            sub_l = l[:k]
            # print(sub_l)
            sub_l.reverse()
            res += sub_l
            # print(res)
            l = l[k:]
        # If there are elements remained (less than k), just add to the end
        if l:
            res += l
        # Create a new linked list
        h = n = ListNode(0)
        for i in res:
            n.next = ListNode(i)
            n = n.next
        return h.next
```

Beacues this approach creates some new lists, it will cost a larger memory usage.

This problem can also be solved by linked-list-method.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        # Set a new head, and self.cut is a global variable to record current node
        self.cut = dummy = ListNode(0)
        # A function to reverse nodes from l to r
        def reverse(l, r):
            prev = None
            newFirst = l
            # Reverse linked node from l to r
            while l != r:
                l.next, l, prev = prev, l.next, l
            l.next = prev
            # Add the reversed linked node into result
            self.cut.next = r
            self.cut = newFirst
        
        newNext = head
        while newNext:
            l = r = newNext
            for i in range(k-1):
                r = r.next
                if not r:
                    break
                newNext = r.next
            # If there are less than k noeds, just add the remained linked list
            if not r:
                self.cut.next = l
                break
            
            reverse(l,r)
        return dummy.next
```

### Conclusion

- A magic method to reverse linked list:
```python
# Reverse linked node from l to r
while l != r:
    l.next, l, prev = prev, l.next, l
l.next = prev
# The head of new reversed linked list is l
```
