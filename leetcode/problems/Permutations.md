## Approach

[Problem link](https://leetcode.com/problems/permutations/)

- My approach

A very problem by using rescuring method.

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def traceback(sub_res, l):
            if len(l) == 0:
                res.append(sub_res)
            else:
                # In each layer of program, select one number add at the end of sub_res
                for i in range(len(l)):
                    traceback(sub_res+[l[i]], l[:i]+l[i+1:])
        traceback([], nums)
        return res
```
