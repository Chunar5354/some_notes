## Approach

[Problem link](https://leetcode.com/problems/rotate-image/)

- My approach

The magic is finding out the coordinate relationsip of the four elements which are perpendicular to each othe
(找到互相垂直的四个元素的坐标关系).
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Here l-1 because in the first line, we just need to traverse the elements from line[0] to line[len(matrix)-2]
        # (because the last element in the first line will be replaced by the first element)
        l = len(matrix)-1
        s = 0
        for i in range(l):
            # To avoid repeating, for every next line, reduce two edge elements
            for j in range(s, l-s):
                # The four element perpendicular to each other have a coordinate relationsip like this:
                matrix[j][l-i], matrix[l-i][l-j], matrix[l-j][i], matrix[i][j] = matrix[i][j], matrix[j][l-i], matrix[l-i][l-j], matrix[l-j][i]
            s += 1
            # If we get into the center element, return
            if l-s - s <= 0:
                return
```
