## Approach

[Problem link](https://leetcode.com/problems/sudoku-solver/)

This is a complex problem, the best way is recursing. Because we need to try every position for every number, 
and in this process, we must record the status. So the traceback method is a good way.
```python
from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        digits = set(map(str,range(1, 10)))
        r, c = defaultdict(set), defaultdict(set) # use r as the set for 3x3 box
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    r[i//3, j//3].add(board[i][j])
        
        def try_position(i, j):
            # i stands for rows, j stands for columns
            if i > 8: return True
            
            if j == 8:
                next_i = i + 1
                next_j = 0
            else:
                next_i = i
                next_j = j + 1
            # If this positioin has already been filt, goto next
            if board[i][j] != '.':
                return try_position(next_i, next_j)
            
            # filter the available numbers
            cands = digits - r[i] - c[j] - r[i//3, j//3]
            if not cands: 
                return False

            for val in cands:
                board[i][j] = val
                r[i].add(val)
                c[j].add(val)
                r[i//3, j//3].add(val)
                
                # If this number is suitable, go to try next position
                if try_position(next_i, next_j):
                    return True
                # If it's not suitable, reset this positoin to '.'
                else:
                    board[i][j] = '.'
                    r[i].remove(val)
                    c[j].remove(val)
                    r[i//3, j//3].remove(val)
            
            return False
                        
        try_position(0, 0)
```

The magic of recuring is that we can easily record the running status. For the problem which needs to try times by times, 
it's a easy way. 

But actually, it's difficult to design.

### Conclusion

- A good method `set()`
