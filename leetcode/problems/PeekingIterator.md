## 284. Peeking Iterator

[Problem link](https://leetcode.com/problems/peeking-iterator/)

- My approach

Firstly save the values of iterator into a list. And set a index to achieve the next and peek operation.

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())
        self.idx = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        p = self.next()
        self.idx -= 1
        return p
        

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.iterator[self.idx-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.iterator)
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

- Other's approach

The method above needs an extra list to store the values. If we use a varaiable to keep the result of next(), we can achieve the peek() operation. That has only O(1) space complexity.

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.prev = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.prev:
            if self.iterator.hasNext():
                self.prev = self.iterator.next()
        return self.prev
        

    def next(self):
        """
        :rtype: int
        """
        if not self.prev:
            return self.iterator.next()
        else:
            curr = self.prev
            self.prev = None
            return curr
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.prev:
            return True
        return self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

