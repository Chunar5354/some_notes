## 396. Rotate Function

[Problem link](https://leetcode.com/problems/rotate-function/)

- Other's approach

It's like a mathematical method. Since every time rotate the last number to front, all other numbers will be from A[i]*(i-1) to A[i]*i, so we can calculate the sum of A firstly, 
if current sum=num, next sum will be `num-(last_number)*(n-1)+(sum_of_A)-(last-number)`(because las_number add to front will be last_number*0), it can be simplified as 
`num - (last_number)*n + sum_of_A`.

```python
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        num = sum(i*A[i] for i in range(len(A)))
        res = num
        s = sum(A)
        n = len(A)
        for i in range(len(A)):
            new_num = num - A[n-i-1]*n + s
            res = max(res, new_num)
            num = new_num
        return res
```
