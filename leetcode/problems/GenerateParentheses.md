## Solution

[Problem Link](https://leetcode.com/problems/generate-parentheses/)

- My solution

Main idea: every time add a pair of parentheses together into string, add n times.

Ilustrate: First time add `'()'` into string, so the string is `'()'`. And then add `'()'` into `'()'`, there are three place to add.
So the result string canbe `'()()'`(add into first place) or `'(())'`(add into second place) or `'()()'`(add into third place), and
the first and the third are the same. So after adding two pair of parentheses, there are two strings in the answer list:`['()()', 
'(())']`. And there are 5 places to add the third parenthese into string (len(string) + 1).

After adding n times, you can get the answer.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = {0: ['()']}
        # Add n times
        for i in range(1, n):
            res[i] = []
            last_f = res[i-1]
            # Add every string in the list
            for j in range(len(last_f)):
                # For each string, there are len(string)+1 places to insert new '()'
                for k in range(len(last_f[j])):
                    this_s = last_f[j][:k] + '()' + last_f[j][k:]
                    if this_s not in res[i]:
                        res[i].append(this_s)
        return res[n-1]
```

This solution is easy to understand, but has a poor performance (beats 5%)

- Other solution

This problem is also suitable for recursing method, but it's too difficult to understand others' recuring method.

Here is an easy understanding recursing resolution:
```python
class Solution(object):
    def generateParenthesis(self, n):
        # Add n times '(' and n times ')'
        def placeBracket(open_parens, closed_parens, current):
            global result
            # If both of them are zero, that means all of parentheses are ended over
            if closed_parens == 0 and open_parens == 0:
                result.append(''.join(current))
            # If closed_parens > open_parens, that means has added more '(' than ')'
            elif closed_parens > open_parens:
                # Here entends two ways, one way is add ')' after '(', like '()()'
                placeBracket(open_parens, closed_parens - 1, current + [')'])
                if open_parens > 0:
                    # And the other is here, add '(' after '(', like '(())'
                    placeBracket(open_parens - 1, closed_parens, current + ['('])
            # If closed_parens == open_parens (it's impossible that closed_parens < open_parens)
            # add a '(' into string
            else:
                placeBracket(open_parens - 1, closed_parens, current + ['('])

        global result
        result = []
        placeBracket(n, n, [])
        return result
```

We can paint a binary tree at the position of `elif`, one branch is add `(` after `(`, the other is add `)` after `(`

### Conclusion

- Reursing is an important method, but sometimes abstract. We can understand as recursing can divide the program into branches.
