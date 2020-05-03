## Approach

[Problem link](https://leetcode.com/problems/sort-list/)

- My approach

The sort methods which learned in class are not suitable for linked list. To solve this problem, we can fetch the value of the nodes in 
an array firstly, then sort the array and create a new linked list by the sortd array.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort()
        new_head = ListNode(values[0])
        n = new_head
        for i in values[1:]:
            n.next = ListNode(i)
            n = n.next
        return new_head
```

There is a method only use linked list called `merge sort`, see it [here](https://leetcode.com/problems/sort-list/discuss/606584/Python-merge-sort-easy-to-understand).
