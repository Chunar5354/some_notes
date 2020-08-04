## 268. Missing Number

[Problem link](https://leetcode.com/problems/missing-number/)

- My approach

There are many methods to solve this problem.

First, sort the list.

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i] - 1
        return nums[-1] + 1
```

Second, translate it into collection.

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(s)):
            if i not in s:
                return i
        return len(s)
```

- Official solution

There are two ways provided by official solution.

We can use XOR.

```python
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```

Or there is a mathimatical method.

```python
class Solution:
    def missingNumber(self, nums):
        # The sum of 0~n equals to n*(n+1)/2
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```
