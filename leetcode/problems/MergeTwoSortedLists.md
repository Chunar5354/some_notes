## Solution

[Problem Link](https://leetcode.com/problems/merge-two-sorted-lists/)

- My solution:

Main idea is adding all elements of one list to the other list.

Firstly, we need to check which list should be the list being added (check the head node value, and the smaller will be the goal).
Then traverse the sub list, compare each current value of the two list, if the value of sub list is larger than the goal list, 
add the current node of sub list after the current value of goal list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # Check which list should be the list to be added
        if l1.val >= l2.val:
            res = l_goal = l2
            sub_l = l1
        else:
            res = l_goal = l1
            sub_l = l2
        while sub_l:
            # For each list, we shoule create two pointers to store current nodes
            l_last = l_goal
            while l_goal and sub_l.val >= l_goal.val:
                l_last = l_goal
                l_goal = l_goal.next

            mid_sub = sub_l.next  # A middle pointer
            # Update nodes
            sub_l.next = l_last.next
            l_last.next = sub_l
            l_goal = sub_l
            sub_l = mid_sub
        return res
```

Beacuse we created two pointers for each list, and do a lot of magic assignment to update nodes, this solution is kind of complex.
Although ti's fast (beats 99%).

- Others' solution

One good solution is created a third list, and add the elements of two given lists to the third list

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a head of third list
        l3 = ListNode(-1)
        head = l3
        while l1 and l2:
            # Add the smaller node of l1 and l2 into l3
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        # If there are remained nodes in l1 or l2
        if l1:
            l3.next=l1
        if l2:
            l3.next=l2
        return head.next
```

There is another way by using a recursing method
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2
```

### Conclusion

- When facing a problem, firstly should think about stylized method, such as recursing...
