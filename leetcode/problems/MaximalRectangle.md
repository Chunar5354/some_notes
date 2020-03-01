## Approach

[Problem link](https://leetcode.com/problems/maximal-rectangle/)

- My approach

This problem is an extention of [Largest Rectangle In Histogram](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/LargestRectangleInHistogram.md).

Firstly convert the matrix into bar chart(x-axis stands for the columns, y-axis stands for height of columns). 
Then use the method of calculating the maximum area of bar chart for each layer.

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        # Set the x-axis of bar chart
        bar_list = [0] * n
        for i in range(m):
            for j in range(n):
                # If current position is '1', means the height of current bar should plus 1
                if matrix[i][j] == '1':
                    bar_list[j] += 1
                # If current position is '0', means the bar is cut here, so the height of current bar should be reset to 0
                else:
                    bar_list[j] = 0
            # Calculate the max area of current layer
            res = max(res, self.getArea(bar_list))
        return res
    
    # The same method of 'Largest Rectangle In Histogram'
    def getArea(self, l):
        print(l)
        stack = []
        ans = 0
        l = [0] + l + [0]
        for i in range(len(l)):
            while stack and l[i] < l[stack[-1]]:
                # print(stack, l[i])
                crt_h = stack.pop(-1)
                ans = max(ans, (i-stack[-1]-1)*l[crt_h])
            stack.append(i)
        return ans
```
