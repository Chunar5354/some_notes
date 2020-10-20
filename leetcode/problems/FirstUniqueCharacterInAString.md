## 387. First Unique Character in a String

[Problem link](https://leetcode.com/problems/first-unique-character-in-a-string/)

- My approach

Save the characters and their counts in a dictionary, then traverse the array and find the first character that its value in dictionary is 1.

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
```
