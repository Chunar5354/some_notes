## 410. Split Array Largest Sum

[Problem link](https://leetcode.com/problems/split-array-largest-sum/)

- Other's approach

The key point is finding that for a given number target, if the array can be splited into k subarrays where `all the sums of the subarrays are less than target`, and `k is less 
than m`.

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:        
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                # total > threshold means the sum of current subarray is larger than threshold
                if total > threshold:
                    total = num
                    count += 1
                    # count > m means if we want to make all the sums of subarrays are less than threshold,
                    # we must split the array to more than m parts, it's unavailable
                    if count > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid     
            else:
                left = mid + 1
        return left
```

For more explanations, see [here](https://leetcode.com/problems/split-array-largest-sum/discuss/769701/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.)
