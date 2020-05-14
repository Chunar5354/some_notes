## Approach

[Problem link](https://leetcode.com/problems/fraction-to-recurring-decimal/)

- My approach

The key point is doing division level by level and save the remainders, if current remainder is existed, means the next calculate will 
be recurring.

For example:

```
1 / 7
quotient  remainder
0.1       3
0.14      2
0.142     6
0.1428    4
0.14285   5
0.142857  1
0.1428571 3

3 has already appeared，so the recurring decimal is (428571)
```

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = False
        # Deal with negative numbers
        if numerator * denominator < 0:
            neg = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        q, r = divmod(numerator, denominator)
        if neg:
            res = '-' + str(q) + '.'
        else:
            res = str(q) + '.'
        # If r=0, means the result doesn't have recurring decimal
        if r == 0:
            return res[:-1]
        
        num = []
        frac = ''
        while True:
            q, r = divmod(r*10, denominator)
            frac += str(q)
            # If r=0, means the result doesn't have recurring decimal
            if r == 0:
                return res + frac
            # r represents the remainder number, if current remainder number is already existed in num, means the next calculate will be in circle
            if r in num:
                idx = num.index(r)
                break
            num.append(r)
        frac = frac[:idx+1] + '(' + frac[idx+1:] + ')'

        return res + frac
```
