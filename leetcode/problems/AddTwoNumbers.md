## 解题

[题目链接](https://leetcode.com/problems/add-two-numbers/)

仍然是自己hardcode了一个（其实也写了好久），对数据结构还是不太熟悉，要在Python中实现一个链表，自己首先想到的还是借助Python的对象，
最后是使用列表实现的，当然成绩很不理想啦：
```python
class Solution:
    def getlist(self, l, l_list):
        if l.next != None:
            self.getlist(l.next, l_list)
            l_list.append(l.val)
        else:
            l_list.append(l.val)
        return l_list   
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = []
        l2_num = []
        sum = 0
        l1_num = self.getlist(l1, l1_num)
        l2_num = self.getlist(l2, l2_num)
        n = max(len(l1_num), len(l2_num))
        for i in range(n):
            if len(l1_num) > 0:
                l1_val = l1_num.pop(-1)
            else:
                l1_val = 0
            if len(l2_num) > 0:
                l2_val = l2_num.pop(-1)
            else:
                l2_val = 0
            sum += (l1_val + l2_val) * 10 ** (i)
        if sum == 0:
            return ListNode(0)
        else:
            s_sum = str(sum)
            res = {}
            for i in range(len(s_sum)):
                if i == 0:
                    res[i] = ListNode(int(s_sum[i]))
                    res[i].next = None
                else:
                    res[i] = ListNode(int(s_sum[i]))
                    res[i].next = res[i-1]
            return res[len(s_sum)-1]
```
其实绕了很多弯路，比如把输入的链表顺序翻过来倒过去（为了实现正常顺序数字相加），其实就是一个进位的问题，把进位位存下来就好了

参考了一个别人的答案：
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode  # 头结点
        val = 0
        while val or l1 or l2:
            # divmod() 返回商和余数
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            # 每次计算后，将结果作为一个新的结点插入链表尾部
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next
```
这个方案好在使用了链表的头结点，用它作为返回结果，这样就可以在每次运算中顺序在链表后插入新结点

### 结论

- 1. 对于结果要返回链表的程序，使用`头结点`是一个好的选择
- 2. 要活用链表的插入等操作

## 知识点

- 1.`divmod(a, b)`返回a/b的商和余数
- 2.`a // b`结果为a/b的商取整数
- 3.在Python中构建一个链表：
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x       # 数据域
        self.next = None   # 指针域
```
