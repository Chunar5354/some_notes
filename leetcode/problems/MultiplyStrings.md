## Approach

[Problem link](https://leetcode.com/problems/multiply-strings/)

- My approach

The fastest way is using `str()` and `int()` method in python, but obviously it's not the intention.

My idea is converting str into int one digit by one.
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        res = ''
        # Convert string into integer
        for i in range(len(num1)):
            n1 += (int(num1[len(num1)-i-1])*(10**i))
        for i in range(len(num2)):
            n2 += (int(num2[len(num2)-i-1])*(10**i))
        mul = n1 * n2
        # Convert integer into string
        while mul >= 10:
            mul, r = divmod(mul, 10)
            res = str(r) + res
        return str(mul)+res
```

But that's also a 'directly convert' method.

- Other's approach

Multiply digit by digit, and add in all.
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        result = [0] * (n + m)
        for i, c1 in enumerate(num1[::-1]):
            carry = 0
            # After this 'for', result stores num1's current digit * num2, in descending order
            for j, c2 in enumerate(num2[::-1]):
                current = int(c1) * int(c2) + carry + result[i+j]
                carry, result[i+j] = divmod(current, 10)
            result[i+m] = carry

        return ''.join(map(str, result[::-1])).lstrip('0') or '0'
```

The magic is using carry and different position in result.
