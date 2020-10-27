## 391. Perfect Rectangle

[Problem link](https://leetcode.com/problems/perfect-rectangle/)

- My approach

If the rectangles can build up a perfect rectangle, the sum of all the areas of rectangles must equal to the area of the perfect rectangle. And the final figure must have 
just 4 points(left-bottom, right-bottom, left-top and right-top).

```python
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mem = set()
        area = 0
        
        for r in rectangles:
            left_bottom = (r[0], r[1])
            right_bottom = (r[2], r[1])
            left_top = (r[0], r[3])
            right_top = (r[2], r[3])
            area += (r[2]-r[0]) * (r[3]-r[1])
            for p in (left_bottom, right_bottom, left_top, right_top):
                if p in mem:  # if p in mem, means current point is merged by two rectangles, so it is not a edge point now
                    mem.remove(p)
                else:
                    mem.add(p)
        if len(mem) != 4:
            return False
        rt, lb = max(mem), min(mem)
        if area == (rt[0]-lb[0])*(rt[1]-lb[1]):
            return True
        return False
        
```
