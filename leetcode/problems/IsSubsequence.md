## 392. Is Subsequence

[Problem link](https://leetcode.com/problems/is-subsequence/)

- My approach

Use two pointers and check if t[i] == s[j] in order.

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i_s = i_t = 0
        while i_t < len(t):
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1
            if i_s == len(s):
                return True
        return False
```
