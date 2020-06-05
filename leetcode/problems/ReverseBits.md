## Approach

[Problem link](https://leetcode.com/problems/reverse-bits/)

- My approach

Translate the integer to string, and reverse the string then translate ie back.

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        # When using bin(), there is a '0b' prefix of thhe result, we need to delete it
        s = str(bin(n))[2:]
        # Make up zeros to 32 length
        while len(s) < 32:
            s = '0' + s
        s = s[::-1]
        return int(s, 2)
```

There are some methods only use integer from official solution.

- Official approach

Create another integer and move bits from given number to the answer bit by bit.

```python
class Solution:
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            # n&1 means only deal with the last bit every time
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
```

And there is a method to reverse a byte only using bit operations.

```python
def reverseByte(byte):
    return (byte * 0x0202020202 & 0x010884422010) % 1023
```

For more details please see official solution.
