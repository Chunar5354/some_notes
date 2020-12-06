## 438. Find All Anagrams in a String

[Problem link](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

- My approach

Use dictionary as a slide window. If all the counts of characters in the window equals the counts in p, means it's a anagram.

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        l = len(p)
        dicP = {}
        for c in p:
            if c in dicP:
                dicP[c] += 1
            else:
                dicP[c] = 1
        
        dicS = {}
        for i in range(l):
            if s[i] in dicS:
                dicS[s[i]] += 1
            else:
                dicS[s[i]] = 1
        
        res = []
        if dicS == dicP:
            res.append(0)
        for j in range(1, len(s)-l+1):
            # Slide the window
            dicS[s[j-1]] -= 1
            if dicS[s[j-1]] == 0:
                dicS.pop(s[j-1])
            if s[j+l-1] in dicS:
                dicS[s[j+l-1]] += 1
            else:
                dicS[s[j+l-1]] = 1
            if dicS == dicP:
                res.append(j)
        return res
```

