> In recent days, there is something wrong with my VPN. So I can't record the questions on github. Today VPN is restored, but because 
these problems were finished some days ago, I can just record them by memory(Question 79~81).

## Approach

[Problem link](https://leetcode.com/problems/word-search/)

- My approach

This is a complex problem. Every single letter has 4 directions, we should consider each direction every time, and if current letter 
is not available, we need to go back to the last letter. So recursing is a good method, because it can record function status.

But my own code didn't work, I tried some ways, but they all failed.
Finally I searched an other's approach.

- Other's approach

This is also a recursing method.

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def recursion(i,j,string,stack):
            '''
            :(i, j): coordinate of letters
            :string: part of given 'word'
            :stack: memory, to save the coordinates which have already been used
            '''
            # Firstly save current coordinate into stack
            stack.append((i,j))
            # If string is '', means there is an available answer
            if not string:
                return True
            # Judge if the left letter is available
            if i-1>=0 and board[i-1][j]==string[0] and (i-1,j) not in stack:
                # The magic is here: finally function recursion will return a bool object, 
                # so the function can directly be used to judge
                if recursion(i-1,j,string[1:],stack):
                    return True
                else:
                    stack.pop()
            # Such as left, judge every directions
            if i+1<len(board) and board[i+1][j]==string[0] and (i+1,j) not in stack:
                if recursion(i+1,j,string[1:],stack):
                    return True
                else:
                    stack.pop()
            if j+1<len(board[0]) and board[i][j+1]==string[0] and (i,j+1) not in stack:
                if recursion(i,j+1,string[1:],stack):
                    return True
                else:
                    stack.pop()
            if j-1>=0 and board[i][j-1]==string[0] and (i,j-1) not in stack:
                if recursion(i,j-1,string[1:],stack):
                    return True
                else:
                    stack.pop()
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Firstly need to find if word[0] is in the given 'board'
                if board[i][j]==word[0]:
                    stack = []
                    if recursion(i,j,word[1:],stack):
                        return True
        # If the function doesn't return, means there is no available answer
        return False
```

## Knowledge

In recursing function, if need to traceback, we can try to let the function returns a `bool object`, so that we can 
directly use the function to judge.
