## 292. Nim Game

[Problem link](https://leetcode.com/problems/nim-game/)

- My approach

The secret of nim game is: if you can take at most m elements, every time you can make the remained elements to the multiple of `m+1`, then you can must win.

So if the number is already a multiply of `m+1` at the beginning, you should lose.

In this problem, m=3, so we just check if n is a multiple of 4.

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```
