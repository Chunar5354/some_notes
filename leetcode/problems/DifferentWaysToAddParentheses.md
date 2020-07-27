## 241. Different Ways to Add Parentheses

[Problem link](https://leetcode.com/problems/different-ways-to-add-parentheses/)

- My approach

I wanted to use recursing method with memory, but it failed. Because this problem can;t use memory.

- Other's approach

This method is called `divide and conquer`. For every operator, we divide the experssion to two parts: left and right. And calculate all the posible answers of left and right, 
save them as an array. Then we can calculate all the numbers in left and right array with current operator.

```python
class Solution:
    def diffWaysToCompute(self, input):
        # If current input is a number, means the only res it itself
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])  # All the possible answer from left
                res2 = self.diffWaysToCompute(input[i+1:])  # All the possible answer from right
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
```
