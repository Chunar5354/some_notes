## Approach

[Problem link](https://leetcode.com/problems/add-binary/)

- My approach

One idea is add two strings position by position.
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Considering carry, firstly add a '0' at the beginning of a and b
        a = '0' + a
        b = '0' + b
        carry = 0
        res = ''
        i = len(a)
        j = len(b)
        while i and j:
            # Plus with carry
            current_n = int(a[i-1]) + int(b[j-1]) + carry
            # If overflowed, current number should reduce 2, and set carry to 1
            if current_n > 1:
                current_n -= 2
                carry = 1
            else:
                carry = 0
            res = str(current_n) + res
            i -= 1
            j -= 1
        # a and b may have different length
        while i:
            current_n = int(a[i-1]) + carry
            if current_n > 1:
                current_n -= 2
                carry = 1
            else:
                carry = 0
            res = str(current_n) + res
            i -= 1
        while j:
            current_n = int(b[j-1]) + carry
            if current_n > 1:
                current_n -= 2
                carry = 1
            else:
                carry = 0
            res = str(current_n) + res
            j -= 1
        # Finally there may be a '0' at the start of res
        if res[0] == '0':
            return res[1:]
        return res
```

And the second idea is transform a and b into integer, then plus them, and transform the answer into binary string.
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == b == '0':
            return '0'
        m = len(a)
        n = len(b)
        numa = 0
        numb = 0
        # Transform a and b into integer
        for i in range(m):
            numa += int(a[m-i-1]) * 2**i
        for j in range(n):
            numb += int(b[n-j-1]) * 2**j
        sum_ab = numa + numb
        res = ''
        # Transform the answer into binary string
        while sum_ab:
            current_n = sum_ab % 2
            sum_ab = sum_ab // 2
            res = str(current_n) + res
        return res
```
