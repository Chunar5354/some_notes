## Approach

[Problem link](https://leetcode.com/problems/excel-sheet-column-number/)

- My approach

There are two ideas: one is from add from right to left and each time multiply `26**i`. And the second is add from left to right, each time 
multiply the answer by 26.

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[len(s)-i-1])-64)*26**i
        return res
```

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for c in s:
            res = res*26 + (ord(c)-ord('A')+1)
        return res
```
