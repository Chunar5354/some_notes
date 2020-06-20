## Approach

[Problem link](https://leetcode.com/problems/isomorphic-strings/)

- My approach

Use two dictionaries to save the map of characters. When finding one character maps to more than one characters, return False.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}
        for i in range(len(s)):
            # Map from s to t
            if s[i] in dic_s.keys():
                if dic_s[s[i]] != t[i]:
                    return False
            else:
                dic_s[s[i]] = t[i]
            # Map from t to s
            if t[i] in dic_t.keys():
                if dic_t[t[i]] != s[i]:
                    return False
            else:
                dic_t[t[i]] = s[i]
        return True
```

- Other's approach

There is a very clear method by using `zip()`.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
```
