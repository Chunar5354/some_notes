## Approach

[Problem link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- My approach

Because it's a sorted array, therre are no duplicated elements, the simplest way in Python is:
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
```

But obviously that's not the intention of questioners.

The second approach uses a lot of `if-else` to judge situations:
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        m = max(nums)
        # If the first number is bigger than the last, means the max number is in middle
        if nums[0] > nums[-1]:
            # If target < nums[0], means if exist, target must between max anf the last number ([max:-1])
            if nums[0] > target:
                if nums[-1] < target:
                    return -1
                else:
                    for i in range(len(nums)):
                        n = nums[len(nums)-i-1]
                        if n == target:
                            return len(nums) - i - 1
                        if n == m:
                            return -1
            # If target =< nums[0], means target is in [0:max]
            else:
                for i in range(len(nums)):
                    if nums[i] == target:
                        return i
                    if nums[i] == max:
                        return -1
        # If nums[0] <= nums[-1], means this array is in asending order, just traverse it
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        return -1
```

This approach can run very fast(beats 90%). But it's hard to calculate its runtime complexity.

- Other approach

In the topic, it mentioned the runtime complexity must be in `O(log n)`. O(log n) usually stands with `dichotomy`（二分法）, 
there is a code:
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid =int((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[left]<=nums[mid]:
                if nums[left]<=target< nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
```

### Conclusioin

- O(log n) runtime complexity and dichotomy.
