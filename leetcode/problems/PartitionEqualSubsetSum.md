## 416. Partition Equal Subset Sum

[Problem link](https://leetcode.com/problems/partition-equal-subset-sum/)

- Other's approach

The key point is checking if the numbers in nums can sum to `sum(nums)/2`.

There are two solutions:

1.Dynamic programming.

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2
        
        dp = [False] * (target+1)
        dp[0] = True
        # dp[i] stands for if number i can be sumed or not
        for n in nums:
            # at the end of the loop, i=n, because dp[0]=True, so at end dp[i] will be set to True
            for i in range(target, n-1, -1):
                dp[i] |= dp[i-n]  # if i-n can be sumed, because n is in nums, i can be sumed
                if dp[target]:
                    return True
        
        return dp[target]
```

2.Greet and DFS.

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2
        nums.sort()
        nums.reverse()  # descending order
        mem = set()
        
        def helper(idx, curr):
            if curr == target:
                return True
            for i in range(idx, len(nums)):
                # beacuse nums is in descending order, every time get the maximum number
                if i not in mem and nums[i]+curr <= target:
                    mem.add(i)
                    if helper(i+1, curr+nums[i]):
                        return True
            return False
        
        return helper(0, 0)
```
