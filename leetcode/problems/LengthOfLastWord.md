## Approach

[Problem link](https://leetcode.com/problems/length-of-last-word/)

- My approach

An easy problem, jus traverse from right to left, until finding a whitespace.
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        l = len(s)
        c = l - 1
        # Aviod whitespace at the end of s
        while s[c] == ' ' and c > 0:
            c -= 1
        for i in range(c+1):
            n = c - i
            if s[n] == ' ':
                return i
        return (c+1)
```

We can also use Python built-in method `spilt` to transform s to a list.
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        for i in range(len(l)):
            n = len(l) - i - 1
            if l[n]:
                return (len(l[n]))
        return 0
```
