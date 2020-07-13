## 227.Basic Calculator 2

[Problem link](https://leetcode.com/problems/basic-calculator-ii/)

- My approach

My idea is like the method learned in class. Create two stacks to store operators and operands. And the the operator have priority, when meet a operator which priority is 
smaller than the last operator in stack, do one calculating.

```python
class Solution:
    def calculate(self, s: str) -> int:
        s += '#'
        stack_operator = []
        stack_operand = []
        # Set the priority, and a symbol at the end
        d = {'+': 0, '-': 0, '*': 1, '/': 1, '#': -1}
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] not in d:
                # Numbers may be longer than one
                start = i
                while s[i] not in d:
                    i += 1
                stack_operand.append(int(s[start: i]))

            else:
                if not stack_operator or d[s[i]] > d[stack_operator[-1]]:
                    stack_operator.append(s[i])
                    i += 1
                
                else:
                    curr = stack_operator.pop()
                    second = stack_operand.pop()
                    first = stack_operand.pop()
                    if curr == '+':
                        ans = first + second
                    elif curr == '-':
                        ans = first - second
                    elif curr == '*':
                        ans = first * second
                    else:
                        ans = int(first / second)

                    stack_operand.append(ans)

        return stack_operand[0]
```

- Other's approach

The method above can be simplified. We don'e need to create two stacks, which means we can calculator every time without pushing operators into a stack.

```python
class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sig, s = 0, [], '+', s + '+'
        for i in s:
            if i in '0123456789':
                num = 10 * num + int(i)
            if i in '+-*/':
                if sig == '+':
                    stack.append(num)
                elif sig == '-':
                    stack.append(-num)
                elif sig == '*':
                    stack.append(stack.pop() * num)
                elif sig == '/':
                    stack.append(int(stack.pop() / num))
                # sig stands for the last operator
                sig = i
                num = 0 
        return sum(stack)
```
