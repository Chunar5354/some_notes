## 304. Range Sum Query 2D - Immutable

[Problem link](https://leetcode.com/problems/range-sum-query-2d-immutable/)

- My approach

This problem is an extention of [Range Sum Query](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/RangeSumQuery.md)

We can save the sum as in `Range Sum Query` row by row. And when calculate the whole sum, add the rows together.

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.num = []
        # self.num[i][j+1] stands for the sum of matrix[i][:j+1]
        for r in matrix:
            curr = r[:]
            for i in range(1, len(r)):
                curr[i] = curr[i-1] + r[i]
            curr = [0] + curr
            self.num.append(curr)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2+1):
            res += self.num[r][col2+1] - self.num[r][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

Or we can save the sum od squares. self.num[i+1][j+1] here stands for the sum of matrix[:i+1][:j+1]

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.num = []
        if not matrix:
            return
        for i in range(len(matrix)+1):
            self.num.append([0]*(len(matrix[0])+1))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.num[i+1][j+1] = matrix[i][j] + self.num[i+1][j] + self.num[i][j+1] - self.num[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.num[row2+1][col2+1] - self.num[row1][col2+1] - self.num[row2+1][col1] + self.num[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```
