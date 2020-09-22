## 345. Reverse Vowels of a String

[Problem link](https://leetcode.com/problems/reverse-vowels-of-a-string/)

- My approach

Use two pointers l and r, when both of them pooint at vowels, swap them.

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        c = list(s)
        l = 0
        r = len(c) - 1
        
        while l < r:
            if c[l] in v and c[r] in v:
                c[l], c[r] = c[r], c[l]
                l += 1
                r -= 1
            if c[l] not in v:
                l += 1
            if c[r] not in v:
                r -= 1
        
        return ''.join(c)
```
