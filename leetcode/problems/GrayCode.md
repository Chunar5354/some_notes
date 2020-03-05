## Approach

[Problem link](https://leetcode.com/problems/gray-code/)

- My approach

`Two number differ in only one bit` means XOR（异或） these two numbers, and the answer will only have one '1' in all the bits.

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for _ in range(2**n):
            for j in range(n):
                # XOR the last number in res and current 2**j
                # becaues 2**j has only one '1' bit
                num = abs(res[-1]^(2**j))
                if num not in res:
                    res.append(num)
                    break
        return res
```

And there is a very smart method from others.

- Other's approach

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            res.append(i ^ (i >> 1))    # I want to know why?
        return res
```

I think it's a mathematical magic.

## Knowledge

In Python, XOR operation is `a ^ b`
