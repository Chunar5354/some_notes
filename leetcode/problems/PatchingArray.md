## 330. Patching Array

[Problem link](https://leetcode.com/problems/patching-array/)

- My approach

My idea is using `2^i`,but it failed.

- Other's approach

There is a very smart method. And [here](https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation) is the explanation.

The key point is `miss` stands for the maximum sum we can reach. And if nums[i] is out of the range, add nums[i] to miss.

```python
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:   # loop till miss = max of the covered range + 1 = (K+1)
                                                    # if nums[i] > miss then nums[i] is out of range even after patching miss e.g. 23 in [1,2,4,23,43]
                miss += nums[i]   # get to the max of the covered range + 1, where +1 comes from initializing miss to be 1
                i += 1
            else:
                miss += miss   # patch miss and lift miss from (K+1) to (2K+2) for finding the new (K+1) for the remaining numbers in nums
                patch += 1     # no. of patches + 1
        return patch
```
