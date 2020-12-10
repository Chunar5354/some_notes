## 443. String Compression

[Problem link](https://leetcode.com/problems/string-compression/)

- My approach

Add the answers at the tail ot chars, then pop the front elements.

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)
        i = 0
        while i < l:
            chars.append(chars[i])
            if i+1 < l and chars[i] == chars[i+1]:
                start = i
                i += 1
                while i < l and chars[i] == chars[start]:
                    i += 1
                length = i - start
                chars += list(str(length))
            else:
                i += 1
        for _ in range(l):
            chars.pop(0)
        return len(chars)
```
