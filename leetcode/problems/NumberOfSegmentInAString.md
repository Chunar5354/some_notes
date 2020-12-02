## 434. Number of Segments in a String

[Problem link](https://leetcode.com/problems/number-of-segments-in-a-string/)

- My approach

Count the whitespaces with other characters.

```python
class Solution:
    def countSegments(self, s: str) -> int:
        s = s + ' '
        res = 0
        for i in range(1, len(s)):
            if s[i] == ' ':
                if s[i-1] != ' ':
                    res += 1
        return res
```
