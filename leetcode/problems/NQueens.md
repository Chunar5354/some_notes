## Approach

[Problem link]()

- My solution

A little difficult problem, I have learnt it in class. Using recursing method to try every position.

Firstly, my code is like this, but it `failed`.
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_list = []
        res = []
        
        # Because every time we insert 'Q' into a new row, we just need to check columns and diagonal.
        def judge(r, c, p):
            for pos in p:
                if pos[1] == c or abs(pos[0]-r) == abs(pos[1]-c):
                    return False
            return True
        
        def traceback(l, position):
            if l == n:
                # Problem here
                return res_list.append(res)

            for i in range(n):
                for p in position:
                    current_line = ['.']*n
                    # If current position is available, insert a 'Q' at this position, and go to next row
                    if judge(l, i, position):
                        current_line[i] = 'Q'
                        current_line = ''.join(current_line)
                        res.append(current_line)
                        # Problem here
                        return traceback(l+1, position+[[l, i]])
        
        traceback(0, [[-1, -1]])
        return res_list
```

This code has a problem. In the code aboce where commentd by `Problrm here`.

By using `return` or not, this code will return different result. There may be short of elements or extra elements in 
he final result.

Then I search for others' approach, and get an idea that `replace the part of making result strings`. The code like this:
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res_list = []
        
        def judge(r, c, p):
            for pos in p:
                if pos[1] == c or abs(pos[0]-r) == abs(pos[1]-c):
                    return False
            return True
        
        def traceback(l, position):
            # Now we make result string here
            if l == n:
                res = []
                for p in position:
                    current_line = ['.']*n
                    current_line[p[1]] = 'Q'
                    current_line = ''.join(current_line)
                    res.append(current_line)
                return res_list.append(res)

            # And we just deal with position here
            for i in range(n):
                if judge(l, i, position):
                    traceback(l+1, position+[[l, i]])
        
        traceback(0, [])
        return res_list
```

This time it works.

And then we can simplify `position` to a one-bit array.
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def traceback(l, position):
            if l == n:
                current_res = []
                for i in position:
                    base_list = ['.']*n
                    base_list[i] = 'Q'
                    current_res.append(''.join(base_list))
                res.append(current_res)
                return
            for i in range(n):
                if judge(l, i, position):
                    # Now position is an one-bit array, its index stands for row
                    traceback(l+1, position+[i])
                    
        def judge(r, c, position):
            for pr, pc in enumerate(position):
                if pc == c or abs(pr-r) == abs(pc-c):
                    return False
            return True
        
        traceback(0, [])
        return res
```
