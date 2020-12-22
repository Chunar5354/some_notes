## 452. Minimum Number of Arrows to Burst Balloons

[Problem link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

- My approach

If one arrow can burst two balloons, means the two balloons have overlap. And if we sort the balloons with the start point, the overlap can be described as that the end point 
of the second balloon is smaller than the first balloon.

For more balloons, we can keep a varaible stands for the right edge, when a new balloon comes, if its start point is smaller than the right edge, it can be burst by the same 
arrow with the group before. Then modify the right edge with the minimum end point(to avoid missing the balloons in middle)

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        right = points[0][1]
        i = 1
        arrows = 1
        while i < len(points):
            if points[i][0] <= right:
                # current balloon can be burst with the arrow before, modify the right edge
                right = min(right, points[i][1])
            else:
                # current balloon need a new arrow to burst, and the new right edge is the end point of current balloon
                arrows += 1
                right = points[i][1]
            i += 1
        return arrows
```
