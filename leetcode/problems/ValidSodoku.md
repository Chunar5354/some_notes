## Approach

[Problem link](https://leetcode.com/problems/valid-sudoku/)

- My approach

Just set every sub areas(lines, columns and 3x3 squares) into a list. Then use `count()` method, if count of some element is larger than 1,
return False.

```python
class Solution:
    # A function to check if there is a element appears more than once
    def jud_list(self, l):
        for i in l:
            if i != '.' and l.count(i) > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Lines
        for sub_b in board:
            res = self.jud_list(sub_b)
            if not res:
                return False
        # Columns
        for j in range(9):
            sub_l = [l[j] for l in board]
            res = self.jud_list(sub_l)
            if not res:
                return False
        # 3x3 squares
        for a in range(3):
            for b in range(3):
                sub_s = board[3*a][3*b:3*(b+1)] + board[3*a+1][3*b:3*(b+1)] + board[3*a+2][3*b:3*(b+1)]
                # print(sub_s)
                res = self.jud_list(sub_s)
                if not res:
                    return False
        return True
```

That's a force method, but unexpectedly, it has a good performance(beats 99%).

- Other's approach

There is a very concise approach
```
class Solution:
    def isValidSudoku(self, board):
        seen = []
        # For each element, store them in a tuple with their serial number of lines, columns and 3x3 squares
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
        # Beacuse tuple is a unchangeable object, we can use set() method to translate the list into a set,
        # and if their length are different, return False
        return len(seen) == len(set(seen))
```

He uses a magic way to store elements with their unique `serial number(line, column and 3x3 square)`. And then use `set()` method 
to check if there are same elements with same serial number.
