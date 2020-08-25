## 307. Range Sum Query - Mutable

[Problem link](https://leetcode.com/problems/range-sum-query-mutable/)

- My approach

My idea is us the method of []() to save the sums, and save the updated positions in an dictionary. When calculate the whole sum, reduce the numbers in the dictionary.

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = nums[:]
        for i in range(1, len(nums)):
            self.sum[i] = self.sum[i] + self.sum[i-1]
        self.sum = [0] + self.sum
        self.diff = {}

    def update(self, i: int, val: int) -> None:
        self.diff[i] = val

    def sumRange(self, i: int, j: int) -> int:
        diff = 0
        for k in self.diff:
            # print(k)
            if i <= k <= j:
                diff += self.sum[k+1] - self.sum[k] - self.diff[k]
                # print(self.sum[k+1], self.sum[k], self.diff[k])
        return self.sum[j+1] - self.sum[i] - diff
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
```

- Official approach

There is a more smarter method by dividing the nums to `sqrt(n)` parts.

```python
class NumArray:
    def __init__(self, nums):
        self.N = len(nums)
        self.size = int(self.N ** 0.5) + 1
        self.A = [0] * self.N
        self.bucket = [0] * self.size  # bucket[i] stands for the sum of [i:i+sqrt(N)]
        for i, val in enumerate(nums):
            self.update(i, val)
            
    def update(self, i, val):
        bidx = i // self.size
        self.bucket[bidx] += val - self.A[i]
        self.A[i] = val
        print(self.bucket, self.A)
        
    def sumRange(self, i, j):
        idx, jdx = i//self.size, j//self.size
        # print(self.bucket)
        total = sum(self.bucket[idx:jdx+1])
        total -= sum(self.A[idx*self.size:i])
        total -= sum(self.A[j+1:(jdx+1)*self.size])
        return total
```
