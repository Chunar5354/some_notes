## Approach

[Problem link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

- My approach

This is a hard problem, my approaches were all time exceeded.

- Other's approach

This approach uses a stack to store some ascending parts(like [1, 3, 5, 6] in [2, 1, 3, 5, 6, 2]).
And when the height of current bar is smaller than the last bar in stack, go to calculate the area.

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        # Firstly add a [0] at the beginning and end
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            # If current height is smaller than the last one in stack, means the start of 'ascending sequence' needs to change
            # and before change it, calculate the area with the bars in stack now.
            while stack and heights[stack[-1]] > heights[i]:
                crt = stack.pop(-1)
                # Because it's ascending order, the largest area of current bar equals to (the height of current bar) * (the distance
                # between current bar and the rightest bar in ascendng order)
                res = max(res, (i-stack[-1]-1)*heights[crt])
            stack.append(i)
        return res
            
```
