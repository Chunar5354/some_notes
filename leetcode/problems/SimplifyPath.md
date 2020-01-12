## Approach

[Problem link](https://leetcode.com/problems/simplify-path/)

- My solution

My idea is transform the string into a list, then delete '.' and '..' by law.
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        # Set a memory to store valid path(not '', '.' or '..')
        memory = []
        for i in range(len(l)):
            if l[i] not in ['', '.', '..']:
                memory.append(i)
            # '.' can be passed
            if l[i] == '.':
                l[i] = ''
            # If meet a '..', set '..' and the last element which is not '' to ''
            if l[i] == '..':
                for k in range(len(memory)):
                    if l[memory[len(memory)-k-1]] != '':
                        l[memory[len(memory)-k-1]] = ''
                        break
                l[i] = ''
        j = 1
        # Delete all the '' in l except the first element
        while j < len(l):
            if l[j] == '':
                l.pop(j)
            else:
                j += 1
        res = '/'.join(l)
        if not res:
            return '/'
        return res
```

And there is a more clear method used `stack` with the same idea.
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split("/")
        stack = []
        for item in split:
            # Avoid '' and '.'
            if item and item != '.':
                # When meet a '..', delete the last element in stack
                if item == '..' and stack:
                    stack.pop()
                elif item != '..':
                    stack.append(item)
        return '/' + '/'.join(stack)
```

I should practice to use the classical method like stack.
