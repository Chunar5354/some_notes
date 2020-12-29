## 459. Repeated Substring Pattern

[Problem link](https://leetcode.com/problems/repeated-substring-pattern/)

- My approach

Traverse s, snd for every index i, check if all the s[i:i+i]  == s[:i].

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(l):
            if i == l-1:
                return False
            if l % (i+1) == 0:
                valid = True
                for j in range(i+1, l, i+1):
                    if s[j:j+i+1] != s[:i+1]:
                        valid = False
                        break
                if valid:
                    return True
        return False
```

- Othre's approach

If a string contains repested pattern, when we cut the first character and last character and connect the two new substrings(make it as a circle), the original 
string should be contained in the new string `s[1:] + s[:-1]`.

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
```

