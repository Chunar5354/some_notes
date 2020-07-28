## 242. Valid Anagram

[Problem link](https://leetcode.com/problems/valid-anagram/)

- My approach

We can save the characters in two lists and sort the lists. If there is an anagram, the two sorted lists will be the same.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return ls == lt
```

Or we can save the characters in a dictionary.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 0
        
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 0
        
        return dic_s == dic_t
```
