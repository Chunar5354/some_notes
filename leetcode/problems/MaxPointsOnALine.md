## Approach

[Problem link](https://leetcode.com/problems/max-points-on-a-line/)

- My approach

The key point is to calculate `slope`. All points with the same slope for a point are on a same line.

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        res = 0
        for i in range(len(points)-1):
            dic = {}
            same_points = 0
            for j in range(i+1, len(points)):
                # If current point is same as points[i], they will be on the same line
                if points[i] == points[j]:
                    same_points += 1
                    continue
                # If the x coordinate values are the same, slpoe is infinity
                if points[j][0]-points[i][0] == 0:
                    current_k = float('inf')
                # Calculate the slope, here mutiply a 10 can avoid float number overflow mistake
                else:
                    current_k = 10*(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                # If current slope is existed, current point is on that line, else there can be a new line
                if current_k in dic:
                    dic[current_k] += 1
                else:
                    dic[current_k] = 1
            
            if not dic:
                res = max(res, same_points)
            else:
                res = max(res, max(dic.values())+same_points)
        return res+1
```

- Knowledge

There is a interesting phenomenon: When calculating the slpoe, if there are two points which are very close, for example:

```
points: (0, 0), (94911150, 94911151), (94911151, 94911152)
slopes: 94911150/94911151, 94911151/94911152

The two slopes are all 0.9999999894638303, but these three points are not on a line
```

This error is due to `float number overflow`. To avoid this error we can `multiply` a number which is larger than 1, as the code above:

```python
current_k = 10*(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
```

For eaxmple:
```
The answer of 10*94911150/94911151 is 9.999999894638302, 
and 10*94911151/94911152 equals to 9.999999894638304
```

According to my understanding, this method is `amplify error`.

The real principle is related to floating number representation and calculation methods.

For more explanation, you can see [here](https://zhuanlan.zhihu.com/p/28162086) or read chapter 2 of *Computer Systems A Programmer's Perspective*.
