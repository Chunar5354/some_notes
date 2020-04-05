## Approach

[Problem link](https://leetcode.com/problems/triangle/)

Reverse the original triangle and modify it that every element(triagnle[i][j]) equals to the minimum of two adjacent elements of the last 
level(min(triangle[i-1][j], triangle[i-1][j+1]).

And finally the minimun path is saved in triangle[-1][0].

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle.reverse()
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i-1][j], triangle[i-1][j+1])
        return triangle[-1][0]
```
