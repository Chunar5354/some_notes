## 240. Search a 2D Matrix II

[Problem link](https://leetcode.com/problems/search-a-2d-matrix-ii/)

- My approach

My idea is using recursing method with memory.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        mem = set()
        self.find = False
        
        def helper(r, c):
            if self.find:
                return
            if matrix[r][c] == target:
                self.find = True
                return
            mem.add((r, c))
            if r < m-1 and (r+1, c) not in mem and matrix[r+1][c] <= target:
                helper(r+1, c)
            if c < n-1 and (r, c+1) not in mem and matrix[r][c+1] <= target:
                helper(r, c+1)
        
        helper(0, 0)
        return self.find
```

- Others approach

This problem can also be solved by iterative method. But if we start at the top-left corner, there are too many situations need to consider. Because numbers both right and below 
may larger then current number. 

But if we start from down-left corner,  it will be more easier. If current number is larger than the target, the answer is at the top. And if current number is 
smaller than the target, the answer is at right.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        r = m-1
        c = 0
        
        while r >= 0 and c <= n-1:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
```
