## 447. Number of Boomerangs

[Problem link](https://leetcode.com/problems/number-of-boomerangs/)

- My approach

The key point is for every point finding out how many other points have the same distance from it. Use a two level dictionary to find this.

And if the number of same distance points of current point is n, to construct boomerang, we need to pick two points, and the order is matter, so the count of current boomerangs 
equals to `n*(n-1)`.

```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dic = collections.defaultdict(dict)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                length = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                if length in dic[i]:
                    dic[i][length] += 1
                else:
                    dic[i][length] = 1
                if length in dic[j]:
                    dic[j][length] += 1
                else:
                    dic[j][length] = 1
        res = 0
        for k1 in dic:
            for k2 in dic[k1]:
                curr = dic[k1][k2]
                if curr >= 2:
                    res += (curr-1)*curr
        return res
```
