## 292. Nim Game

[Problem link](https://leetcode.com/problems/nim-game/)

- My approach

The secret of nim game is: if you can take at most m elements, every time you can make the remained elements to the multiple of m, then you can must win.

So if the number is already a multiply of m at the beginning, you should lose.

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```
