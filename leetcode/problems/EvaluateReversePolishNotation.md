## Approach

[Problem link](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

- My approach

The key point is to find the two operand of the operator.

To solve this problem, I use a recursing method and pop the elements from right to left. If current element is an operator, its operands 
are the two left adjacent numbers or expressions.

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = '+-*/'
        def helper():
            # Find two operands of current operator
            if tokens[-1] in operator:
                crt_operator = tokens.pop()
                if tokens[-1] not in operator:
                    right_number = tokens.pop()
                else:
                    right_number = helper()
                if tokens[-1] not in operator:
                    left_number = tokens.pop()
                else:
                    left_number = helper()
            else:
                return tokens.pop()
            left_number = int(left_number)
            right_number = int(right_number)
            
            # Calculate
            if crt_operator == '+':
                crt_ans = left_number + right_number
                # print(left_number, '+', right_number)
            elif crt_operator == '-':
                crt_ans = left_number - right_number
                # print(left_number, '-', right_number)
            elif crt_operator == '*':
                crt_ans = left_number * right_number
                # print(left_number, '*', right_number)
            else:
                crt_ans = int(left_number / right_number)
                # print(left_number, '/', right_number)
            # print(crt_ans)
            return crt_ans
        return helper()   
```

There is a more concise method using stack.

- Other's approach

This method is more like the method studing in class. Pop the given array from left to end, when meet numbers, push them into stack, 
and when meet operators, pop two numbers from stack and calculate the answer, then pop the answer into stack.

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            # Push numbers into stack
            if i not in '+-*/':
                ans = int(i)
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                ans = b + a
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                ans = b - a
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                ans = b * a
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                ans = int(b / a)
            # Push answer into stack
            stack.append(ans)
        return stack[0]
```
