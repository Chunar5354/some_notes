## 436. Find Right Interval

[Problem link](https://leetcode.com/problems/find-right-interval/)

- My approach

The start of intervals are unique, so we can use dictionary to save the starts. Then in order to find the minimum larger strat, we sort the keyys of 
dictionary and use binary search to find the position to insert current end, that position is the minimum larger start.

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # save the starts in dictionary and sort the keys
        dic = {}
        for i in range(len(intervals)):
            dic[intervals[i][0]] = i
        keys = list(dic.keys())
        keys.sort()
        
        res = []
        for j in intervals:
            if j[1] > keys[-1]:
                res.append(-1)
            else:
                # binary search to find the position
                l, r = 0, len(keys)-1
                while l < r:
                    mid = (l+r) // 2
                    if keys[mid] < j[1]:
                        l = mid+1
                    elif keys[mid] > j[1]:
                        r = mid
                    else:
                        l = mid
                        break
                res.append(dic[keys[l]])
        return res
```
