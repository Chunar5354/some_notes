## 419. Battleships in a Board

[Problem link](https://leetcode.com/problems/battleships-in-a-board/submissions/)

- My approach

Because every ship is sparated, we can just find the start of vertical ship and end of horizontal ship, and ignore other 'X'.

```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    # find the end of vertical ship and start of horizontal ship
                    if j >= len(board[0])-1 or board[i][j+1] == '.':
                        if i-1 < 0 or board[i-1][j] == '.':
                            res += 1

        return res
```
