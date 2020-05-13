## Approach

[Problem link](https://leetcode.com/problems/compare-version-numbers/)

- My approach

Split the giving string with '.' and check nubers from high position to low position(from left to right).

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        # Compare numbers from left to right
        while l1 and l2:
            v1 = int(l1.pop(0))
            v2 = int(l2.pop(0))
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        # If there are numbers remained, check if they are all 0
        if l1:
            for i in l1:
                if int(i) != 0:
                    return 1
        if l2:
            for i in l2:
                if int(i) != 0:
                    return -1
        return 0
            
            
```
