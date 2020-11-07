## 402. Remove K Digits

[Problem link](https://leetcode.com/problems/remove-k-digits/)

- My approach

Traverse from left to right, when meet a number that num[i] > num[i+1], pop num[i], do this for k times.

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        num = num + '0'
        for _ in range(k):
            if int(num) == 0:
                return '0'
            for i in range(len(num)-1):
                if num[i] > num[i+1]:
                    num = num[:i] + num[i+1:]
                    break
        n = int(num[:-1])
        return str(n)
```

The solution above has O(k*n) time complexity.

- Other's approach

This is a simplified solution by using stack. Save the numbers in stack from left to right, and when meet a number that is less than stack[-1], 
pop all the larger numbers at the end of stack. And do this for k times.

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and stack[-1] > n and k > 0:
                k -= 1
                stack.pop()
            stack.append(n)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        if not stack:
            return '0'
        
        return str(int(''.join(stack)))
```
