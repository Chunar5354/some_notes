## 237. Delete Node in a Linked List

[Problem link](https://leetcode.com/problems/delete-node-in-a-linked-list/)

- My approach

This problem asks us to delete a node in a linked list. But it doesn't give the head, there is only a target node.

The solution is: firstly swap the value of current node and the next node, then delete the next node.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val, node.next.val = node.next.val, node.val
        node.next = node.next.next
```
