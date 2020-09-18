## 341. Flatten Nested List Iterator

[Problem link](https://leetcode.com/problems/flatten-nested-list-iterator/)

- My approach

Firstly using recursing method to save the numbers in nestedlist into a list.

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ni = []
        self._dealWithList(nestedList)
    
    def next(self) -> int:  
        return self.ni.pop(0)
    
    def hasNext(self) -> bool:
        return self.ni != []
        
    def _dealWithList(self, l):
        for n in l:
            if n.isInteger():
                self.ni.append(n.getInteger())
            else:
                self._dealWithList(n.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

```
