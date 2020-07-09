## Approach

[Problem link](https://leetcode.com/problems/rectangle-area/)

- My approach

I was confused by how to judge if there is overlap area. Finally I got a wrong method.

- Other's approach

But actually, it's very easy to judge the overlap. We just need to check one left edge with the other's right edge, and the top edge with the other's bottom edge.

```python
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        width, height = min(C, G) - max(A, E), min(D, H) - max(B, F)
        # If both width and height are positive, means there is a overlap, and ita area equals to height times to width
        overlap = height * width if (height > 0 and width > 0) else 0
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap
```

And in some static language such as java, doing a subtraction may cause overflow. 

We can change the judgement like this:

```python
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if E > C or B > H or A > G or F > D:
            overlap = 0
        else:
            overlap = (min(C, G)-max(A, E)) * (min(D, H)-max(B, F))
        return (C-A)*(D-B) + (G-E)*(H-F) - overlap
```
