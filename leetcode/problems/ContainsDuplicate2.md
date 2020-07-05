## Approach

[Problem link](https://leetcode.com/problems/contains-duplicate-ii/)

- My approach

This is an easy problem, we can traverse the nums and check if current number nums[i] is in the next k elements nums[i:i+k].

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            if nums[i] in set(nums[i+1: i+1+k]):
                return True
        return False
```

Or we can just check every k+1 length parts of nums if the set of them has the same length with their own.

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        if k >= len(nums)-1:
            return True

        for i in range(len(nums)-k):
            if len(set(nums[i:i+k+1])) != k+1:
                return True
        return False
```

Or we can save the numbers as {value:index} in a dictionary, and check if the dinstinct of current number and its last same number is smaller than k.

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for idx, value in enumerate(nums):
            if value in dic:
                diff = idx - dic[value]
                if diff <= k:
                    return True
            dic[value] = idx
        return False
```
