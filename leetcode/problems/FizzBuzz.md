## 412. Fizz Buzz

[Problem link](https://leetcode.com/problems/fizz-buzz/)

- My approach

Just check if the number is mutiple of 5 or mutiple of 3 or both.

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
                continue
            if i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res
```
