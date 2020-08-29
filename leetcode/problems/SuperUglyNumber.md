## 313. Super Ugly Number

[Problem link](https://leetcode.com/problems/super-ugly-number/)

- My approach

We can see it as an extention of [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/).

Create an array of pointers to primes. And every time find the minimum `primes[i]*res[p[i]]`, add it to the end of res.

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pointers = [0] * len(primes)
        res = [1]
        for _ in range(n):
            curr = min(primes[i]*res[pointers[i]] for i in range(len(primes)))
            res.append(curr)
            for i in range(len(primes)):
                if res[pointers[i]]*primes[i] == curr:
                    pointers[i] += 1
        return res[-2]
```
