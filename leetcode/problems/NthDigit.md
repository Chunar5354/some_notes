## 400. Nth Digit

[Problem link](https://leetcode.com/problems/nth-digit/)

- My approach

There is a regular that th whole length of t-bit numbers equals to `t*9*10^(t-1)`(0-9, 10-99 ...).

So we can firstly determine the length of the number which contains nth digit.

After finding out the length, we can know which is the number by using the rmained n. And let `r=n%t`, so r means the index of the digits.

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        t = 1
        j = 9
        while n > j:
            n -= j
            t += 1
            j = t * 9 * 10**(t-1)
        
        q = n // t  # means there are q numbers between target number and the start of t-length number
        r = n % t  # r means the target digit is rth of target number
             
        if r == 0:  # the last digit of previous number
            return (10**(t-1)+q-1) % 10
        else:
            s = str(10**(t-1)+q)
            return s[r-1]
```
