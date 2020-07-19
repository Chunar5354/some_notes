## 233.Number of Digit One

[Problem link](https://leetcode.com/problems/number-of-digit-one/)

- My approach

There are some regular patterns of number ones.

There are one '1' in 0-9.

And in 0-99, each x0-x9 has a '1', and 10-19 has 10 '1'. So there are `1*10+10=20` '1' in 0-99.

And in 0-999, each x00-x99 has 20 '1', and 100-199 has 100 '1', so there are `20*10+100=300` '1' in 0-999.
 
So we can find the regular pattern. If we count the digit as i, the count of '1' in all the i-digit numbers will be `i * 10^(i-1)`.

Here we see an example.

```
If the given number is 123, we count the digit start with 0 and from right to left.

The digit of 3 is 0, so current count of '1' is [3 * 0 * 10^(0-1)=0]. And because 3 is larger than 1, we must consider the special '1xx` numbers, the number is [10^i].
So the total count of '1' in this digit is 1.

Then the digit of 2 is 1, current count is [2 * 1 * 10^(1-1)=2]. And 2 is larger than 1, consider the special `10~19`, the number is [10^1=10], the total count is 12.

Then the digit of 1 is 2, current count is [1 * 2 * 10^(2-1)=20]. And 1 equals to 1, which means it doesn't fill the whole special area '100~199'. For this example, the special 
numbers are just '100~122`, they can provide 23 '1'. The total count is 43.

So the answer is [1 + 12 + 43=56]
```

Here is the code

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        i = 0
        remain = 0
        res = 0
        while n > 0:
            curr_remain = n % 10
            n = n // 10
            if curr_remain > 1:
                res += curr_remain * i * 10**(i-1) + 10**i
            # If current digit is 1, we need the remain number to calculate
            elif curr_remain == 1:
                res += i*10**(i-1) + remain + 1
                      
            remain = curr_remain*10**i + remain
            i += 1
        return int(res)
```
