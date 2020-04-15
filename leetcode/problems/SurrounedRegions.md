## Approach

[Problem link](https://leetcode.com/problems/surrounded-regions/)

- My approach

The idea is starting from the four edges, when meet a 'O' in edge, go to find all the connected 'O'.

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board
        m = len(board)
        n = len(board[0])
        visited = []
        def helper(r, c):
            '''
            Find all the connected 'O', and save the positions into visited
            '''
            visited.append((r, c))
            if r-1 >= 0 and board[r-1][c] == 'O' and (r-1, c) not in visited:
                helper(r-1, c)
            if r+1 <= m-1 and board[r+1][c] == 'O' and (r+1, c) not in visited:
                helper(r+1, c)
            if c-1 >= 0 and board[r][c-1] == 'O' and (r, c-1) not in visited:
                helper(r, c-1)
            if c+1 <= n-1 and board[r][c+1] == 'O' and (r, c+1) not in visited:
                helper(r, c+1)
        # Traverse four edges
        for i in range(n):
            if board[0][i] == 'O':
                helper(0, i)
        for i in range(m):
            if board[i][n-1] == 'O':
                helper(i, n-1)
        for i in range(n):
            if board[m-1][i] == 'O':
                helper(m-1, i)
        for i in range(m):
            if board[i][0] == 'O':
                helper(i, 0)
        # Finally the 'O' which posiiton is in visited should not be changed
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
```

But the code is lengthy and complex, inspired by other's approach, I improved this method.

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board
        m = len(board)
        n = len(board[0])
        # Create a list stands for four direction step
        step = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def helper(r, c):
            # Change the 'O' which doesn'e need to change to another letter 'I'
            if board[r][c] == 'O':
                board[r][c] = 'I'
                # Next position can be calculated by current position and the elements in step
                for x, y in step:
                    if 0 <= r+x <= m-1 and 0 <= c+y <= n-1:
                        helper(r+x, c+y)
        # Four edges
        for i in range(m):
            helper(i, 0)
            helper(i, n-1)
        for j in range(n):
            helper(0, j)
            helper(m-1, j)
        # Create a dictionary to change letters
        change = {'X': 'X', 'O': 'X', 'I': 'O'}
        for i in range(m):
            for j in range(n):
                board[i][j] = change[board[i][j]]
```

The new code can run much more faster.
