## 383. Ransom Note

[Problem link](https://leetcode.com/problems/ransom-note/)

- My approach

Save characters in dictionary and check if the count of characters in magazine is enough for ransom

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for s in magazine:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        
        for s in ransomNote:
            if s not in dic or dic[s] == 0:
                return False
            else:
                dic[s] -= 1
        return True
```

