## Approach

[Problem link](https://leetcode.com/problems/excel-sheet-column-title/)

- My approach

The key point is doing division. Current remainder represends a character, add it at front. Then divide until the quotient is less than 26.

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 26:
            n, crt_res = divmod(n, 26)
            # If the remainder is 0, this is a special case, because there is no character to repersent 0
            # for example, the answer of 52 is 'AZ'
            if crt_res == 0:
                return chr(n+63)+res+'Z'
            res = chr(crt_res+64) + res
        return chr(n+64) + res
```

And there is a more clear method by others.

- Other's approach

He saves the characters into a list, this is more intutive.

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = ""
        while n > 0:
            result += capitals[(n-1)%26]
            n = (n-1) // 26
        return result[::-1]
```
