## Approach

[Problem link](https://leetcode.com/problems/search-a-2d-matrix/)

- My approach

Because it's a sorted matrix, we can compare the target and last element of every row, if target is smaller than the last element, 
the result must be in current row or not exist.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False
        for m in range(len(matrix)):
            if matrix[m][-1] >= target:
                for i in matrix[m]:
                    if i == target:
                        return True
                return False
        return False
```
