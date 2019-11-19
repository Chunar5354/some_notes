## Solving

Sorry, from today on, the articles will be writed in English

[Problem Link](https://leetcode.com/problems/valid-parentheses/)

Find the valid parentheses.My thought is creating a dictionary, the keys are three left parentheses, and their value
is a list. Traverse the given string, add every index of left parenthese at the end of lists. When a right parenthese
appears, pop the last element of the corresponding left list, and check if the difference of the indexs of this pair 
of parentheses (to avoid the situation such as `[(]`). Finally, three lists in the dictionary should be empty, otherwise, 
return False.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': [],
             '[': [],
             '{': [],}
        for index, val in enumerate(s):
            # the three if has the same structer
            if val == ')':
                # if there is no corresponding left parenthese, return False
                if len(d['(']) == 0:
                    return False
                else:
                    last_left = d['('].pop(-1)
                    # between a pair of parentheses, there must be even elements
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
        # if finally the three lists are all empty, that means the given string is valid
        if d['('] == d['['] == d['{'] == []:
            return True
        else:
            return False
```

It'a gooo solution, and it's fast(beat 95%). But it has a complex coding.

Look at the offical solution, it use stack to store every character. When we meet a right parenthese, check the top of the stack, 
if it can pair with current right parenthese, pop the top and go on, otherwise, return False.

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

### Conclution

- Stack is a magic thing.
