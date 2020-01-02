## Approach

[Problem link](https://leetcode.com/problems/permutation-sequence/)

- My approach

I wanted to calcuate the total permutation of n numbers and find the kth element, but it's time exceeded.

By referencing other's approach, I get a method to find the regulation of permutation, about`(n-1)!`.
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Set all str(number) into a list
        arr = [str(i + 1) for i in range(n)]
        res = []
        # Calculate factorial of n
        fac = 1
        for i in range(1, n+1):
            fac *= i

        k -= 1
        while n:
            # In permutation answers, the value of first position depends on the value of (k/(n-1)!),
            # because for each number as the beginning, there are (n-1)! results in he permutation,
            # like 
            fac = int(fac/n)
            index, k = divmod(k, fac)
            res.append(arr[index])
            arr = arr[:index] + arr[index + 1:]
            n -= 1
            
        return ''.join(res)
```
