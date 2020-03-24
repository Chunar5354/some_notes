## Approach

[Problem link](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

- My approach

To create a height balanced BST, every time we can use the middle element of value list to be the root, and the left part list be 
the left child, right part list be the right child.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traceback(nodes):
            if not nodes:
                return None
            # Current root is the middle number
            idx = len(nodes) // 2
            root = TreeNode(nodes[idx])
            # Left part is the left child, so is right
            root.left = traceback(nodes[:idx])
            root.right = traceback(nodes[idx+1:])
            return root
        return traceback(nums)
```

And this method can run faster if we use index as arguments instead of list.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, lo, hi):
            # Use two indexs as arguments
            if hi < lo:
                return
            mid = (hi + lo) // 2
            head = TreeNode(nums[mid])
            head.right= helper(nums,mid + 1, hi)
            head.left = helper(nums,lo, mid - 1)
            return head
        return helper(nums,0, len(nums) - 1)
```
