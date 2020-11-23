## 421. Maximum XOR of Two Numbers in an Array

[Problem link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

- Other's approach

The key point is to check if the bit ans[i] can be set to 1.

See [here](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/849128/Python-O(32n)-solution-explained) for more explanations.

```python
class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:  # means current bit can be set to 1
                    ans = start
                    break
         
        return ans
```
