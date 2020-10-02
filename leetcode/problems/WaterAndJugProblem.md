## 365. Water and Jug Problem

[Problem link](https://leetcode.com/problems/water-and-jug-problem/)

- Other's approach

The key point is: if z is the multiple of the `gcd`(Greatest common divisor 最大公约数) of x and y, it must be measurable.

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if not z: 
            return True #edge case 
        
        def gcd(x, y): 
            """Return greatest common divisor via Euclidean algo"""
            if x < y:
                x, y = y, x
            while y:
                x, y = y, x%y
            return x
        
        return z <= x + y and z % gcd(x, y) == 0
```
