## Appraoch

[Problem link](https://leetcode.com/problems/basic-calculator/)

- My approach

My idea is using two stacks, one stores operators and the other stores operands and parentheses.

Because there are '-' in the string, firstly I reverse the string to keep the calculator order such as `2-1`.

```python
class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        ope_stack = []
        
        s = '(' + s + ')'
        s = s[::-1]

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == ')':
                num_stack.append(s[i])
            # Calculator the answer between current parentheses
            elif s[i] == '(':
                curr = num_stack.pop()
                while num_stack[-1] != ')':
                    operator = ope_stack.pop()
                    if operator == '+':
                        curr += num_stack.pop()
                    else:
                        curr -= num_stack.pop()
                num_stack.pop()
                # After calculating, push the answer back into stack
                num_stack.append(curr)
            # operators
            elif s[i] == '+' or s[i] == '-':
                ope_stack.append(s[i])
            # numbers
            else:
                start = i
                # The numbers may be longer than 1
                while s[i] in '0123456789':
                    i += 1
                num_stack.append(int(s[start:i][::-1]))
                continue
            i += 1
        return num_stack[0]                
```

- Official approach

My idea is a little same as official solution, such as using stack.

But official approach is more clearly and it doesn't need to reverse the string.

```python
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
```

Formore explinations please see [official solution](https://leetcode.com/problems/basic-calculator/solution/)
