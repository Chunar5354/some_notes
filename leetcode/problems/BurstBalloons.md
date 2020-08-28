## 312. Burst Balloons

[Problem link](https://leetcode.com/problems/burst-balloons/)

- My approach

My recursing method was time limited exceeded.

- Other's approach

There is a dp method from other's. Here is the [explanation](https://leetcode.com/problems/burst-balloons/discuss/76263/My-readable-Python-~500ms-accepted-solution-with-explanation)

dp[i][j] stands for max coins after the balloons in region (i, j) are burst.

```python
def maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1]+[n for n in nums if n!=0]+[1]
    regional_max_coins = [[0 for i in xrange(len(nums))] for j in xrange(len(nums))]
    for balloons_to_burst in xrange(1, len(nums)-1): # number of balloons in (l,r) region
        for l in xrange(0, len(nums)-balloons_to_burst-1): # for m and r to be assigned legally
            r = l+balloons_to_burst+1
            for m in xrange(l+1,r):
                regional_max_coins[l][r] = max(regional_max_coins[l][r], regional_max_coins[l][m]+regional_max_coins[m][r]+nums[l]*nums[m]*nums[r])
    return regional_max_coins[0][-1]
```
