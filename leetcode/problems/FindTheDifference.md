## 389. Find the Difference

[Problem link](https://leetcode.com/problems/find-the-difference/)

- My approach

Save the characters as {character:count} in dictionary, and find the different count.

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for c in s:
            dic[c] -= 1
            if dic[c] == 0:
                dic.pop(c)
        
        return list(dic.keys())[0]
```
