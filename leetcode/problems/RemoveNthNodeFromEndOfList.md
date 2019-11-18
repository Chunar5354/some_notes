## 解题

[题目链接](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

单链表的题目（凸显出数据结构与算法这门课的重要性，还好选了它），删除指定的节点，有两种方法：

- 1.使用单个指针，计算链表长度
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pass, one pointer
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        d = {1: head}
        node = head
        while node.next:
            node = node.next
            length += 1
            d[length] = node
        if length == 1:
            return None
        # 如果n等于链表长度，头指针就要变化
        if n == length:
            head = d[2]
        else:
            d[length-n].next = d[length+1-n].next
        return head
```

- 2.使用两个指针，fir指针先走n个节点，然后和sec指针一起走，当fir走到头的时候，sec.next就是要删除的节点
```python
# one pass, two pointer
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 为方便对特殊情况（比如单链表长度为1）的处理，在最前面加入一个新的头指针
        s_head = ListNode(0)
        s_head.next = head
        # fir和sec一开始都是新的头指针
        fir = sec = s_head
        # fir先走n个节点
        for i in range(n):
            fir = fir.next
        while fir.next:
            fir = fir.next
            sec = sec.next
        # sec.next是要删除的那个节点，如果它是头结点，那头结点就要变化
        if sec.next == head:
            head = head.next
        else:
            sec.next = sec.next.next
        return head
```

总体来说这道题比较简单，因为了解单链表的原理

用两个指针的方法很棒，自己没有想到

### 结论

- 在处理链表问题的时候，自行为其创建一个`新的头结点`，能把问题变得更普遍性
