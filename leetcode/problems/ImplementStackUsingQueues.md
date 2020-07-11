## Appraoch

[Problem link](https://leetcode.com/problems/implement-stack-using-queues/)

- My approach

In Python, there is a double-ended queue `deque`. It can push or pop elements from both left and right.

So this problem will be easy by using deque.

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        num = self.d.pop()
        self.d.append(num)
        return num    
    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.d) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

And for one-ended queue, we can reverse the elements while pushing.

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.append(x)
        # Push all the elements fromtop and add them to the end
        for _ in range(len(self.d)-1):
            num = self.d.pop(0)
            self.d.append(num)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.d[0]
    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.d) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
