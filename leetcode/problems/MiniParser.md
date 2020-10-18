## 385. Mini Parser

[Problem link](https://leetcode.com/problems/mini-parser/)

- My approach

Firstly traverse the string into a nested list, then construct it to the structure recursively.

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s.split(',')[0]))
        
        # Transerve the string into nested list
        l = []
        stack = [l]
        i = 0
        while i < len(s):
            if s[i] == '[':
                next_level = []
                stack[-1].append(next_level)
                stack.append(next_level)
            elif s[i] == ']':
                stack.pop()
            elif s[i] in '0123456789-':
                start = i
                while s[i] in '0123456789-':
                    i += 1
                stack[-1].append(int(s[start:i]))
                i -= 1
            i += 1
        
        def helper(sl):
            res = NestedInteger()
            if type(sl) == int:
                res.setInteger(sl)
            else:
                res = NestedInteger()
                for ssl in sl:
                    res.add(helper(ssl))
            return res
        
        return helper(l[0])
```
