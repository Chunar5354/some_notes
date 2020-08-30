## 315. Count of Smaller Numbers After Self

[Problem link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

- Other's approach

This problem can be solved by using `binary search tree`. In Python, there is a module `bisect` to achieve this function.

Here is the [explanation](https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/656092/Python-simple-and-clear-bisect-solution-with-explanation-beats-90).

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        res_reversed = []
        for num in reversed(nums):
            sorted_idx = bisect.bisect_left(sorted_nums, num)
            res_reversed.append(sorted_idx)
            bisect.insort(sorted_nums, num)
        
        return reversed(res_reversed)
```
