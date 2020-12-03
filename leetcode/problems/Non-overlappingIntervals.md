## 435. Non-overlapping Intervals

[Problem link](https://leetcode.com/problems/non-overlapping-intervals/)

- My approach

Firstly sort the list with left edge. Then for every current n, if n[0] < start[1], means there is overelap, we should remove current n(res + 1). And if n[1] < start[1], we 
modify start to n, because to make the minimum removing, we need to select the shorter area(they are less possible to be overlap with other areas).

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = 0
        i = 1
        res = 0
        while i < len(intervals):
            # intervals[i][0] < intervals[start][1] means there is overlap
            while i < len(intervals) and intervals[i][0] < intervals[start][1]:
                if intervals[i][1] < intervals[start][1]:  # we select the shortest area
                    start = i
                i += 1
                res += 1
            start = i
            i += 1
        return res
```
