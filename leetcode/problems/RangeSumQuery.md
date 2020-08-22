## 303. Range Sum Query - Immutable

[Problem link](https://leetcode.com/problems/range-sum-query-immutable/)

- My approach

My idea is brout force.

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.l = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.l[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

- Official solution

We can calculate the sum firstly and save them in an array. So we don't need to calculate in every call.

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.res = nums[:]
        for i in range(1, len(nums)):
            self.res[i] = nums[i] + self.res[i-1]
        self.res = [0] + self.res
        
    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1] - self.res[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```
