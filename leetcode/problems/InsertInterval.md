## Approach

[Problem link](https://leetcode.com/problems/insert-interval/)

- My approach

This problem is an extension of [Merge Intervals](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/MergeIntervals.md).
We can use the same method.
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # Firstly add newInterval into intervals
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
```
