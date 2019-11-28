## Approach

[Problem link](https://leetcode.com/problems/divide-two-integers/)

Divide two numbers, and can't use divide or multiplication method. Firstly I want to cumulatively add divisor to dividend. 
But it exceeded.

So without divide and multiplication, if add can't pass, I don't know how to use other methods.

There is an approach from others.
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)
        quotient = 0
        the_sum = divisor
        
        while the_sum <= dividend:
            current_quotient = 1
            # Every time get double 'the_sum', and double 'current_quotient',
            # if double 'the_sum' is larger than dividend, reduce the_sum from divident,
            # then do the same operation to the difference, until divident < divisor
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_quotient += current_quotient
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient
            
        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
```

This approach double current sum every time, like power operation, so it runs fast.

### Conclusion

- An operation about integer range
```python
# Return integer included in [2^32-1, -2^32]
return min(2147483647, max(result, -2147483648))
```
