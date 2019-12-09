## Approach

[Problem link](https://leetcode.com/problems/combination-sum-ii/)

- My approach

This problem is as same as [Combination sum](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/CombinationSum.md). We can also use a recursing method.
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        
        def subSum(l, t, sub_res):
            for i in range(len(l)):
                n = t - l[i]
                if n == 0:
                    res_app = sub_res+[l[i]]
                    if res_app not in self.res:
                        self.res += [res_app]
                    break
                elif n > 0:
                    # Because every elememt can be used just once, so the next layer start with l[i+1]
                    subSum(l[i+1:], n, sub_res+[l[i]])
                else:
                    break
        subSum(candidates, target, [])
        return self.res
```

This approach doesn't run very fast(beats 70%). Because there may be same elements, that will create repeated results.

There is an other's faster approach.
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []
        
        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                # This 'continue' can avoid repeated elements
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        
        backtrack(0, 0, [])
        return res
```
