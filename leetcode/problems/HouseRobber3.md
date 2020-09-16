## 337. House Robber III

[Problem link](https://leetcode.com/problems/house-robber-iii/)

- My approach

Because the thief can't rob the linked nodes, for every node, there maybe two plans: rob current root and not rob current root.

For example, if the tree is like:

```
     3
    / \
   4   5
  / \   \ 
 1   4   1
```

For the left child, he can rob 1+4(without root) or 4(with root). And for the right child, he can rob 1(without root) and 5(with root).

Then for root 3, if the thief robs 3, he can't rob 4 and 5, so the first plan is `3+(1+4)+1`(with root). And if he doesn't rob 3, he can rob the max of left child + the max of right child, the second plan is `max(1+4, 4)+max(1, 5)`(without root). We can do this layer by layer until the root node.

```python
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(n):
            if not n:
                return 0, 0
				
            left_with_root, left_without_root = helper(n.left)
            right_with_root, right_without_root = helper(n.right)
            left = max(left_with_root, left_without_root)
            right = max(right_with_root, right_without_root)
            
            return n.val+left_without_root+right_without_root, left+right
        return max(helper(root))
```
