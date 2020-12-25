## 455. Assign Cookies

[Problem link](https://leetcode.com/problems/assign-cookies/)

- My approach

Sort and traversal s and g and find until s[j] >= g[i].

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        res = 0
        while i < len(g) and j < len(s):
            while s[j] < g[i]:
                j += 1
                if j >= len(s):
                    return res
            res += 1
            i += 1
            j += 1
                
        return res
```
