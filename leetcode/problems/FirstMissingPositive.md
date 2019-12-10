## Approach

[Problem link](https://leetcode.com/problems/first-missing-positive/)

- My approach

Delete the negative integers and sort the array. Then we can easily find the missing number.
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        # Delete negative numbers
        l = [x for x in nums if x > 0]
        if len(l) == 0:
            return 1
        min_n = min(l)
        if min_n > 1:
            return 1
        else:
            # If current integer is in the list, go on and find the larger next number
            while min_n in l:
                min_n += 1
            return min_n
```

There is also a smart approach fron others.
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        holes = {}
        # In holes, the keys stand for target positive numbers
        # Because we are dealing with positive numbers, so the length of nums must contain the target number we are finding
        for i in range(0, len(nums)+1):
            holes[i+1] = True
        if not nums:
            return 1
        # Set all the value of positive integers to 'False'
        for i in range(0, len(nums)):
            if nums[i] > 0:
                holes[nums[i]] = False
        # Now in holes, the keys which value are False are the missing numbers,
        # we just need to find the smallest one
        for i in range(1, len(nums)+2):
            if holes[i]:
                return i
```

In this approach, the magic is because we are dealing with positive integers, the target number must be `smaller than the length 
of nums`.

And this approach is more common because it just use hashmap and traverse. All the languaues have these method.
