## 282. Expression Add Operators

[Problem link](https://leetcode.com/problems/expression-add-operators/)

- My approach

My idea is firstly create all the possible expressions for the given num. Then use the method of [Basic Calculator 2](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/BasicCalculator2.md) 
to calculate the expression.

```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        if num == str(target):
            return [num]

        res = set()
        def helper(idx, exp):
            if idx >= len(num):
                if self.calculate(exp) == target:
                    res.add(exp[:-1])
                return
            # 0 can't be at start of a number
            if num[idx] == '0':
                for e in '+-*':
                    helper(idx+1, exp+num[idx]+e)
            else:
                for i in range(idx, len(num)):
                    for e in '+-*':
                        helper(i+1, exp+num[idx:i+1]+e)
        helper(0, '')
        return res
    
    
    def calculate(self, s: str) -> int:
        num, stack, sig = 0, [], '+'
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
                sig = i
                num = 0 
        return sum(stack)   
```

- Official solution

```python
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return answers
```
