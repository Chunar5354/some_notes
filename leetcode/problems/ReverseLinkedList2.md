## Approach

[Problem link](https://leetcode.com/problems/reverse-linked-list-ii/)

- My solution

Find the edge of the nodes need to reverse, and reverse them one by one.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        end = dummy
        i = 0
        # The right edge gies first
        while i < n-m:
            end = end.next
            i += 1
        start = dummy
        # After right edge goes (n-m) steps, left edge start to go
        i = 0
        while i < m-1:
            start = start.next
            end = end.next
            i += 1
        # Now the target nodes are from start.next to end.next
        final = end.next.next
        judge = start.next
        # Reverse them one by one
        # For example: 2345 -> 3245 -> 4325 -> 5432
        while judge.next != final:
            curr = judge.next
            judge.next = curr.next
            curr.next = start.next
            start.next = curr
        return dummy.next
```

- Other's approach

The approach above can be improved, because we needn't to find the right edge.

There is a simplified approach from someone else.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: return head
        
        pre = dummy = ListNode(-1)
        dummy.next = head
        
        for i in range(m - 1):
            pre = pre.next
        tail = pre.next
        # Only need to find the left edge, and do reverse (n-m) times
        for i in range(n - m):
            temp = pre.next
            pre.next = tail.next
            tail.next = tail.next.next
            pre.next.next = temp
        
        return dummy.next
```

- Official approach

Official solution provides a recursing method. Find the two edges and swap them everytime. The key idea is use function return 
to the last layer to simulate a backward pointer.

```python
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            # print(left, '\n', right)

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            
            # print('after call:', left, '\n', right)
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head
```
