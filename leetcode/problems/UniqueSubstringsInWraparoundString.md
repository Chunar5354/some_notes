## 467. Unique Substrings in Wraparound String

[Problem link](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)

- Other's approach

Since all the substrings are constructed by adjacent characters, we can ignore the specific strings, just find the max length of substrings start with every character.

For example, is p is 'abcdabc', the length pattern will be `4321321`, and the final structer will be {'a':4, 'b':3, 'c':2, 'd':1}, because 'abc' is contained in 'abcd', this 
method can avoid the duplications.

```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dic = {c:1 for c in p}
        l = 1
        for i in range(len(p)-2, -1, -1):  # sea4ch from right to left
            if (ord(p[i+1])-ord(p[i])) % 26 == 1:
                l += 1
                dic[p[i]] = max(dic[p[i]], l)
            else:
                l = 1
        return sum(dic.values())
```
