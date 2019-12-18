## Approach

[Problem link](https://leetcode.com/problems/permutations-ii/)

- My approach

This problem is same as [Permutation](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/Permutations.md), but add duplications. We can also use recursing.
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def traceback(sub_res, l):
            if len(l) == 0:
                if sub_res not in res:
                    res.append(sub_res)
            else:
                for i in range(len(l)):
                    traceback(sub_res+[l[i]], l[:i]+l[i+1:])
        traceback([], nums)
        return res
```

But this method runs very slowly(beats 7%).

- Other's approach

Use three 'for' cycles, without recursing.
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = [[]]        
        
        # Insert every number from nums into ans
        for n in nums:
            new_ans = []
            for l in ans:
                # For each l, insert current number in every position of l
                for i in range(len(l)+1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    # If meet a repeated number, avoid it
                    if i < len(l) and n == l[i]:
                        break
            ans = new_ans
        
        return ans
```
