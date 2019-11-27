## Solution

[Problem link](https://leetcode.com/problems/implement-strstr/)

This is an easy problem, use Python method `index()` can immediately get the answer.
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
```

And it's also easy to traverse the string manually.
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        n = len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
```
