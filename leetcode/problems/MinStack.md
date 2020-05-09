## Approach

[Problem link](https://leetcode.com/problems/min-stack/)

- My approach

In Python we can use `list` to simulate stack.

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

And to improve the speed, we can create another list to store the information of minimum value.

- Other's approach

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_val = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        # If current number is smaller than the minimum number until now, this current number will be the minimum
        if not self._min_val or self._min_val[-1] >= x:
            self._min_val.append(x)

    def pop(self) -> None:
        x = self._stack.pop()
        # If current pop number is the minimum, we need to pop it from self._min_val
        if x == self._min_val[-1]:
            self._min_val.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_val[-1]
```
