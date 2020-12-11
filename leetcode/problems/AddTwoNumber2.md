## 445. Add Two Numbers II

[Problem link](https://leetcode.com/problems/add-two-numbers-ii/)

- My approach

Firstly converse the two linked lists to integer, then add the two integers and converse the sum to linked list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = 0
        while l1:
            n1 = n1*10 + l1.val
            l1 = l1.next
        n2 = 0
        while l2:
            n2 = n2*10 + l2.val
            l2 = l2.next
        
        n = n1 + n2
        if n == 0:
            return ListNode(0)
        res = None
        while n > 0:
            curr = n % 10
            n = n // 10
            curr_node = ListNode(curr)
            curr_node.next = res
            res = curr_node
        return res
```
