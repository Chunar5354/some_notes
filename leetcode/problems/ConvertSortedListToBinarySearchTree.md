## Approach

[Problem link](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

- My approach

This problem is an extension of [Convert Sorted Array To Binasy Search Tree](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/ConvertSortedArrayToBinasySearchTree.md). We can firstly save the value of linked list into an array(list).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes = []
        # Firstly save values into a list
        while head:
            nodes.append(head.val)
            head = head.next
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nodes[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root
        return helper(0, len(nodes)-1)
```
