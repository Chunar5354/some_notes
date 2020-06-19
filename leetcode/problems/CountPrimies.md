## Approach

[Problem link](https://leetcode.com/problems/count-primes/)

- Other's approach

The key idea is when finding a prime number, we can know that all the `k*i` which smaller than n are not prime numbers. And check one by one.

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        # 1 stands for current index is prime number
        res = [1] * n
        res[0] = res[1] = 0
        
        # Here we just need go to sqrt(n)
        for i in range(2,int(n ** 0.5) + 1):
            # When find a prime number, set all 'k*i' to 0
            if res[i]:
                res[2 * i:n:i] = len(res[2 * i:n:i]) * [0]
        return sum(res) 
```
