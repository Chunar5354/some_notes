## Approach

[Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

- My approach

Set a dictionary to count how many times every number appears. When one number appeared moer than two times, remove the remain 
same number.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        dic = {}
        while i < len(nums):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            if dic[nums[i]] > 2:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
```

