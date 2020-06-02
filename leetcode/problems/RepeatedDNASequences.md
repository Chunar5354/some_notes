## Approach

[Problem link](https://leetcode.com/problems/repeated-dna-sequences/)

- My approach

To solve this problem, we can traverse the given string and create a memory to store each 10 length strings. When we meet a string that 
has already in memory, means it's repeated, add it into result.

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        mem = set()
        for i in range(len(s)-9):
            crt_s = s[i:i+10]
            if crt_s in mem:
                res.add(crt_s)
            else:
                mem.add(crt_s)
        return list(res)
```
