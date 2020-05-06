## Approach

[Problem link](https://leetcode.com/problems/reverse-words-in-a-string/)

- My approach

This is an easy problem, just save all the words and compose them to a new string in reverse order.

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        i = 0
        # Save all the words in l
        while i < len(s):
            if s[i] != ' ':
                start = i
                while i < len(s) and s[i] != ' ':
                    i += 1
                l.append(s[start:i])
            else:
                i += 1
        # Compose a new string
        res = ''
        for j in l:
            res = j + ' ' + res
        return res[:-1]
```

The method avove is a general method. This problem can be more easier by Python build-in method `split` and `join`.

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = [i for i in l if i != '']
        l.reverse()
        return ' '.join(l)
```
