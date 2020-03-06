## Approach

[Problem link](https://leetcode.com/problems/subsets-ii/)

- My approach

This is an extension of [Subsets](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/Subsets.md).

We can improve the approach os Subsets.

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for n in range(len(nums)):
            # Every time add current number to the existed answers
            # Add a judge
            res += [i+[nums[n]] for i in res if i+[nums[n]] not in res]
        return res
```

Because there need to judge if current answer has already in the final result list, this mtehod runs slower.

- Other's approach

This problem can also be solved by recursing method(or DFS).

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, idx):
            '''
            :curr: sub list
            :inx: the index of current position
            '''
            res.append(list(curr))
            # If current position is the last one, this branch should be finished
            if idx == len(nums):
                return
            
            prev = None
            # Only need to deal with the elements after current position
            for i in range(idx, len(nums)):
                if nums[i] == prev:
                    continue
                curr.append(nums[i])
                dfs(curr, i+1)
                # This is the key operation, after call the next layer function, pop the last element in curr as a judge
                # So we can keep all the 'curr' in one function layer have the same length
                prev = curr.pop()
                
        dfs([], 0)
        return res
```
