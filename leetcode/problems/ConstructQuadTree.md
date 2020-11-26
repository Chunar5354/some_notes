## 427. Construct Quad Tree

[Problem link](https://leetcode.com/problems/construct-quad-tree/)

- My approach

Recursing + divide and conquer.

```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def divideFour(n): # divide the list into four parts
            l = len(n)
            m = l // 2
            tl = [n[i][:m] for i in range(m)]
            tr = [n[i][m:] for i in range(m)]
            bl = [n[i][:m] for i in range(m, l)]
            br = [n[i][m:] for i in range(m, l)]
            return tl, tr, bl, br
        
        def allSame(n): # check if all the numbers in the list are same
            set_n = set()
            for i in n:
                set_n |= set(i)
                if len(set_n) > 1:
                    return False
            return len(set_n) == 1
        
        def traceback(n):
            if len(n) == 1 or allSame(n):  # current node is a leaf
                curr = Node(n[0][0], True, None, None, None, None)
            else:  # current node is not a leaf
                curr = Node(n[0][0], False, None, None, None, None)
                tl, tr, bl, br = divideFour(n)
                curr.topLeft = traceback(tl)
                curr.topRight = traceback(tr)
                curr.bottomLeft = traceback(bl)
                curr.bottomRight = traceback(br)
            return curr
        
        return traceback(grid) 
```
