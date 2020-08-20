## 300. Longest Increasing Subsequence

[Problem link](https://leetcode.com/problems/longest-increasing-subsequence/)

- My approach

My idea is using dynamic program, dp[i] is the longest increasing subsequence of nums[:i].

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            curr = 1
            for j in range(i):
                # If current number is larger than nums[j], current length of increasing subsequence is dp[j]+1
                if nums[i] > nums[j]:
                    curr = max(curr, dp[j]+1)
            dp[i] = curr
            
        return max(dp)
```

- Official solution

There is an O(nlog(n)) method by using binary search and dynamic. we can consider dp as a container of increasing subsequence. Then we traverse the array nums, every time 
insert(or modify) nums[i] into dp to make dp as increasing order. At last the length of increasing subsequence in dp is the answer. 
(but it not the correct longest increasing subsequence, just the length!)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        size = 0
        for item in nums:
            low, up = 0, size
            # Find the position to insert or modify current number
            while low < up:
                mid = (low + up) // 2
                if dp[mid] < item:
                    low = mid + 1
                else:
                    up = mid
            dp[low] = item
            size = max(size, low + 1)  # length of increasing subsequence
        return size
```
