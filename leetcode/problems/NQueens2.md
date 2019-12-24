## Approach

[Problem link](https://leetcode.com/problems/n-queens-ii/)

- My approach

This problem is the same as [N-Queens](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/NQueens.md), the difference is in this problem, we just need to return the count of available answers.

So we can use the same method, and add a number when find the right answer.
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def traceback(l, position):
            if l == n:
                self.res += 1
                return
            for i in range(n):
                if judge(l, i, position):
                    traceback(l+1, position+[i])
        
        def judge(r, c, position):
            for pr, pc in enumerate(position):
                if pc == c or abs(pr-r) == abs(pc-c):
                    return False
            return True
        traceback(0, [])
        return self.res
```

Then when I looking at others' results, I find a smart method.

It doesn't define a extra function to do the judge, instead by judging with index of rows and columns.
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0]
        def dp(r, rollleft, rollright):
            i = len(r)
            if i == n:
                res[0] += 1
                return
            for j in range(n):
                # res stands for column, the index of elements in res stands for row,
                # rl stands for left diagonal, rr stands for right diagonal.
                # Because all the elements on the left digonal have the same value of (i + j),
                # and all the elements on the right digonal have the same value of (i - j).
                if j not in r and i + j not in rollleft and i - j not in rollright:
                    dp(r + [j], rollleft + [i + j], rollright + [i - j])
        dp([], [], [])
        return res[0]
```
