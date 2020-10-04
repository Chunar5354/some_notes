## 368. Largest Divisible Subset

[Problem link](https://leetcode.com/problems/largest-divisible-subset/)

- My approach

Use dynamic programming, dp[i] stands for the largest divisible subset until nums[i].

```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [[]] * len(nums)
        dp[0] = [nums[0]]
        
        for i in range(1, len(nums)):
            curr = [nums[i]]
            # Traverse nums[:i], is current nums[i] is divisible with dp[i][-1], it is divisible with all dp[i]
            for j in range(i):
                if nums[i] % dp[j][-1] == 0:
                    temp = dp[j] + [nums[i]]
                    if len(temp) > len(curr):
                        curr = temp
            dp[i] = curr

        res = []
        for l in dp:
            if len(l) > len(res):
                res = l
        return res
```

- Other's approach

We can find all the factors of n firstly. For every n, the largest divisible subset equals to the largest divisible subset of its factors plus current n.

```python
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums: return []
        
        nums.sort()
        def find_factors(n):
            factors = []
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    factors.append(i)
                    factors.append(n // i)
            return factors
            
        cache = dict()
        for n in nums:
            factors, subset = find_factors(n), []
            for f in factors:
                if f in cache:
                    if len(cache[f]) > len(subset):
                        subset = cache[f]
            cache[n] = subset + [n]
        return max(cache.values(), key=len)
```
