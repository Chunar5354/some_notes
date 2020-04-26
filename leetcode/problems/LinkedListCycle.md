## Approach

[Problem link](https://leetcode.com/problems/linked-list-cycle/)

- My problem

To check if there is a cycle in linked list, we can traverse the linked list, and check if there is a node which appears twice.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        mem = []
        while head:
            mem.append(head)
            if head.next in mem:
                return True
            head = head.next
        return False
```

And if we change the memory type as a `hash map`, the speed will be increase a lot.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        x = set()
        node = head
        while node:
            x.add(node)
            node = node.next
            if node in x:
                return True
        return False
```

- Official approach

The methods above have `O(n)` space complexity. There is a method which can solve this problem with only `O(1)` space complexity.

The kyp point is using two pointers with `different speed`.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        # p1 goes 1 step every time, and p2 goes 2wteps every time
        # if there is a cycle, finally they will meet
        p1 = head
        p2 = head.next
        while p1 and p2:
            if p1 == p2:
                return True
            p1 = p1.next
            if not p2.next:
                return False
            p2 = p2.next.next
        return False
```
