## Approach

[Problem link](https://leetcode.com/problems/trapping-rain-water/)

- My approach

My idea is `kill the max`. Traverse from left to right, when find a `height[i] < height[i-1]`, check if height[i-1] if the largest height.
If yes, then we reduce height[i-1] to the `second max` value, because how much water can a container store depends on the shorter edge. 
And then if height[i-1] is still larger than height[i], current volumn is `height[i-1]-height[i]`.

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)-1):
            if height[i] < height[i-1]:
                # Find max height of the rest right numbers
                m = max(height[i+1:])
                # If height[i-1] is larger than the max of the rest, reduce it into max
                if m < height[i-1]:
                    height[i-1] = m
                # If after reducing, height[i] is still smaller than height[i-1], calculate the volumn
                if height[i] < height[i-1]:
                    res += (height[i-1]-height[i])
                    # This is important, after calculating, we need to fill the blank(add height[i] as same as height[i-1])
                    height[i] = height[i-1]
                    
        return res
```

This approach calculate volumn one element by one element, and it needs to find a max. So it runs very slowly(beats 5%).

- Other's approach

This approach is the same as `offical approach 4`

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ml, mr = 0, 0
        res = 0
        while l <= r:
            # Find the smaller one in l and r
            if height[l] <= height[r]:
                # ml is the left edge of the left notch
                if height[l] >= ml:
                    ml = height[l]
                # If height[l] is smaller than ml, current volumn is (ml - height[l])
                else:
                    res += ml - height[l]
                l += 1
            else:
                if height[r] >= mr:
                    mr = height[r]
                else:
                    res += mr - height[r]
                r -= 1
        return res
```
