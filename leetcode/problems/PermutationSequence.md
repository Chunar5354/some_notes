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
            # like giving number 3, the total permutation is '123, 132, 213, 231, 312, 321',
            # and there are (3-1)!=2*1 elements which start with '1', '2' or '3'
            
            # After cealing with the first number, use the same method do deal with the second number,
            # but this time, k is the remainder(余数) of (k/(n-1)!), and fac is (n-2)!,
            # until n = 0.
            fac = int(fac/n)
            index, k = divmod(k, fac)
            res.append(arr[index])
            arr = arr[:index] + arr[index + 1:]
            n -= 1
            
        return ''.join(res)
```
