## 289. Game of Life

[Problem link](https://leetcode.com/problems/game-of-life/)

- My approach

Firstly create a copy of board, and check every cell by he rules to modify board.

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m = len(board)
        n = len(board[0])
        
        temp = []
        for i in range(m):
            temp.append(board[i][:])
            
        def ifLive(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            else:
                return temp[r][c]
        
        
        for i in range(m):
            for j in range(n):
                s = sum(ifLive(i+d[0], j+d[1]) for d in directions)
                if temp[i][j] == 1:
                    if s == 2 or s == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if s == 3:
                        board[i][j] = 1         
```

To get O(1) space complex, we can modify board in-place. If current cell is 0 but will change to 1, we set it to -1, and if current cell is 1 and will change to 0, we set it to 2.
After modifying by the rules, traverse board and change 2 to 0, and -1 to 1.

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m = len(board)
        n = len(board[0])
        
        def ifLive(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            else:
                if board[r][c] > 0:
                    return 1
                else:
                    return 0
        
        
        for i in range(m):
            for j in range(n):
                s = sum(ifLive(i+d[0], j+d[1]) for d in directions)
                if board[i][j] == 1:
                    if s < 2 or s > 3:
                        board[i][j] = 2  # current 1 and need to be changed to 0
                else:
                    if s == 3:
                        board[i][j] = -1  # current 0 and need to be changed to 1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1
```
