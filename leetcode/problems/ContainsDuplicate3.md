## Approach

[Problem link](https://leetcode.com/problems/contains-duplicate-iii/)

- My approach

Firstly I think this problem is complicated because firstly my code was time limit exceeded.

But after seeing other's approach, I realized I just need to set a quick checking ot the situation of "t=0". So this problem becomes easy.

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if t == 0 and len(nums) == len(set(nums)):
            return False
        
        for i in range(len(nums)):
            for j in range(k):
                if i+j+1 >= len(nums):
                    break
                if abs(nums[i] - nums[i+j+1]) <= t:
                    return True
        return False
```
