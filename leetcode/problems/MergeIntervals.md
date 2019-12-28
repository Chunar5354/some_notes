## Approach

[Problem link](https://leetcode.com/problems/merge-intervals/)

- My approach

My idea is as same as the second official solution.

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        # Firstly sort the list
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # Check the last list in res and current list in intervals
            # If the end of res[-1] is larger than the start os intervals[i], means these two lists should be merged
            if res[-1][-1] >= intervals[i][0]:
                # The start of new list is the minimum of two lists, 
                # and the end of new list is the maximumm of two lists
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][-1], intervals[i][-1])]
            # If the end of res[-1] is smaller than the start os intervals[i], just append intervals[i] to res
            else:
                res.append(intervals[i])
        return res
```

### Conclusion

- Two-dimensional in Python can be sorted by `sort()`
