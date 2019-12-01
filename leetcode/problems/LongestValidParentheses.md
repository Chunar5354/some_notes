## Approach

[Problem link](https://leetcode.com/problems/longest-valid-parentheses/)

Firstly I thought it in a complex way, and get confused.

There are two good approaches provided by official.

- 1.Stack

Set a stack to store index of every char in s, when find a '(', just push in stack. And when find a ')', pop the top of stack, 
then calculte the difference between current index and the new top (this new pop stands for the index before the 
`start` of a valid sub_string)
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Firstly push a '-1' in stack, to avoid the situation 's[0] == "("'
        stack = [-1,]
        res = num = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)   # This makes stack[-1] is always the last index before the start '('
                if stack == []:
                    stack.append(i)
                else:
                    # stack[-1] is the index before the start of this whole sub valid parentheses
                    res = max(res, i - stack[-1])
        return res
```

The magic is store `the index before 'start "("'`

- 2.Left and right

This is a smart approach which traverses 's' two times, one from left to right, one from right to left.

For the traversing from left to right, count the number of '('(l) and ')'(r). When `l=r`, means that this a valid sub string. When `r>l`, 
meand current sub string is not valid, then reset `l=r=0`, continue traverse.

And from right to left is same, but the judgement is `l>r`
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        l = r = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            # When l = r, length = 2*r
            if l == r:
                res = max(res, 2*r)
            # If r > l, reset
            elif r > l:
                l = r = 0
        l = r = 0
        for i in range(len(s)):
            n = len(s) - i -1
            if s[n] == ')':
                r += 1
            else:
                l += 1
            if l == r:
                res = max(res, 2*l)
            elif l > r:
                l = r = 0
        return res
```

This approach can save space.
