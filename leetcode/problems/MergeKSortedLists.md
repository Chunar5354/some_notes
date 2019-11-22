## Solution

[Problem Link](https://leetcode.com/problems/merge-k-sorted-lists/)

- My solution

There is a problem named [Merge Two Lists]() before, my idea is: do merge two lists method one by one.

Such as a list `l` has 4 listnodes, firstly, merge l[0] and l[1] and get the result l01. Them merge l01 and l[2], get the result l012, 
then merge l012 and l[3], the result l0123 is the final result.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergetwo(self, l1, l2):
        res = head = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        # print(head.next)
        return head.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        res = None
        # Merge two lists one by one
        for i in range(len(lists)):
            res = self.mergetwo(res, lists[i])
        return res
```

But this method causes a problem: for each merging, list l1 will be longer and longer. So it will costs a lot of time.

There is an optimized approach for the approach above:
```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        # Here is a magic!
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
```

There is a magic method in this approach. Every time, it combines n pairs of lists to merge (n is len(lists)/2*time).

For example, a given list with 6 elements. First time, merge l[0] with l[1], l[2] with l[3], l[4] with l[5], and the results are:
l01, l23, l45. Second time, merge l01 with l23, the result is l0123. Finally, merge l0123 and l45, and it's the final result.

By this way, we can recude merging times, and the list to merge will not be very long. So it can save time.

- Fastest approach

The fastest approach in Python is putting all node.val in a list, then sort the list. Finally create a new listnode.
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        h = p = ListNode(0)
        for l in lists:
            while l:
                # Save all val into list
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            # Create a new ListNode
            p.next = ListNode(x)
            p = p.next
        return h.next
```

### Conclusion

- Magic method to combine two elements together each time for a list:
```python
amount = len(lists)
        interval = 1
        while interval < amount:
            # Pay attention to 'amount - interval'
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
```
