## Solving

Sorry, from today on, the articles will be writed in English

[题目链接](https://leetcode.com/problems/valid-parentheses/)

Find the valid parentheses.My thought is creating a dictionary, the keys are three left parentheses, and their value
is a list. Traverse the given string, add every index of left parenthese at the end of lists. When a right parenthese
appears, pop the last element of the corresponding left list, and check if the difference of the indexs of this pair 
of parentheses (to avoid the situation such as `[(]`). Finally, three lists in the dictionary should be empty, otherwise, 
return False.

查找合法的括号，自己的想法是创建一个字典，键为三个左括号，对应的值都为一个列表，遍历字符串，把每一个左括号的索引值添加到列表末尾
每当出现一个右括号的时候，就去掉对应的左括号列表中的最后一个索引值去掉，并查看左右两个括号的索引值之差（避免`[)]`这种情况），
到最后，三个左括号对应的列表都应该为空，否则就返回False

```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': [],
             '[': [],
             '{': [],}
        for index, val in enumerate(s):
            # 这里三个if判断的形式是一样的，只是对应的键不同
            if val == ')':
                # 如果没有对应的左括号了，就返回False
                if len(d['(']) == 0:
                    return False
                else:
                    last_left = d['('].pop(-1)
                    # 一对左右括号之间必须是偶数个元素
                    if (index-last_left) % 2 == 0:
                        return False
            elif val == ']':
                if len(d['[']) == 0:
                    return False
                else:
                    last_left = d['['].pop(-1)
                    if (index-last_left) % 2 == 0:
                        return False
            elif val == '}':
                if len(d['{']) == 0:
                    return False
                else:
                    last_left = d['{'].pop(-1)
                    if (index-last_left) % 2 == 0:
                        return False
            else:
                d[val].append(index)
        # 如果最后三个列表都是空的，说明给出的字符串是合法的
        if d['('] == d['['] == d['{'] == []:
            return True
        else:
            return False
```

A good solution is to use stack

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
```
