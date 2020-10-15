## 382. Linked List Random Node

[Problem link](https://leetcode.com/problems/linked-list-random-node/)

- My approach

Store the values in a list, and use `random.choice()` to get values randomly.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.l = []
        while head:
            self.l.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.l)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

- Follow up

This problem has a follow-up version: if the length of linked list is very large and we don't know, how to get random value?

Traverse the linked list, and for every node, we have a probability to modify it or not, the probability equals to `1/n`, which n is the index of node.

So the probability of one node can reach the end equals to `1* 1/2 * 1/3 * ... * 1/n`.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.n = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 1
        curr = self.n
        val = curr.val
        
        while curr.next:
            num = random.random()
            count += 1
            if num <= (1/count):  # modify
                val = curr.next.val
            curr = curr.next
        return val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```
