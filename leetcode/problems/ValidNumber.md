## Approach

[Problem link](https://leetcode.com/problems/valid-number/)

- My approach

We can use python built-in method `float` directly.
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
```

Or consider every condition.
```python
class Solution:
    def isNumber(self, s: str) -> bool:
        n = set('0123456789')
        # If there is no number in s, it's not valid
        if not set(s) & n:
            return False
        valid = '+-0123456789e.'
        start = 0
        end = len(s) - 1
        # Delete whitespaces at the edge
        while start < len(s) and s[start] == ' ':
            start += 1
        while end > 0 and s[end] == ' ':
            end -= 1
        s = s[start: end+1]
        # Unvalid characters
        for i in s:
            if i not in valid:
                return False
        # About 'e'
        if 'e' in s:
            e = s.index('e')
            # Left of 'e' or right of 'e' must be a number
            # And there can't be a '.' right of 'e'
            # And there can't be more than one 'e'
            if not set(s[:e]) & n or not set(s[e:]) & n or '.' in s[e+1:] or 'e' in s[e+1:]:
                return False
        # About '.', there can only be one '.'
        if s.count('.') > 1:
            return False
        # About '+-'
        # '+' and '-' can only be at the beginning or next 'e'
        # And except the first element, there can be at most 2 '+' or '-'
        if s[1:].count('+') > 1 or s[1:].count('-') > 1:
            return False
        if '+' in s[1:]:
            index = s[1:].index('+')
            if s[index] != 'e':
                return False
        if '-' in s[1:]:
            index = s[1:].index('-')
            if s[index] != 'e':
                return False
        return True
```
