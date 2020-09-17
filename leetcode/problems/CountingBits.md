## 338. Counting Bits

[Problem link](https://leetcode.com/problems/counting-bits/)

- My approach

The key idea of this problem is calculate current bits by the numbers in front.

My idea is every `n=2^p` has only one 1, and numbers after 2^p is 1 + numbers in front.

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        p = 0
        idx = 0
        
        for i in range(1, num+1):
            if i == 2**p:  # When meet a 2^p, reset idx
                idx = 0
                p += 1
            res.append(res[idx]+1)
            idx += 1
        return res
```

- Other's approach

There is a more clear method by using `bit moving`.

If the last bit of current i is 0, the number of 1 equals to i >> 1, and if it is 1, the number of 1 equals to i>>1 + 1.

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            if i & 1:
                ans.append(1 + ans[i >> 1])
            else:
                ans.append(ans[i >> 1])
        
        return ans
```
