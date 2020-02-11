## Aproach

[Problem link](https://leetcode.com/problems/combinations/)

- My approach

My idea is using rescuring method, like finding full combination, but end at 'k' numbers.

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        self.res = []
        def traceback(sub_l, num):
            if len(sub_l) == k:
                self.res.append(sub_l)
                return
            else:
                for j in range(len(num)):
                    # To avoid duplication, next layer num will start at j+1
                    traceback(sub_l+[num[j]], num[j+1:])
        traceback([], nums)
        return self.res
```

But rescuring always takes a long time, there is a faster approach from others.

- Other's approach

```python
class Solution:
    def combine(self, n: int, k: int):
        nums = list(range(1, k + 1)) + [n + 1]
        ans = []
        idx = 0
        while idx < k:
            ans.append(nums[:k])
            idx = 0
            # When there are neighboring numbers in nums, update nums(ans) in-place
            while idx < k and nums[idx + 1] == nums[idx] + 1:
                nums[idx] = idx + 1
                idx += 1
            nums[idx] += 1
        return ans
```

He found a regular that when there are neighboring numbers in the sun answer `nums`, the last neighboring need to be changed.

- Built-in approach

Python has a built-in method to solve combination problems.

```python
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = combinations([j for j in range(1,n+1)],k)
        lst = [i for i in l]
        return lst
```

## Knowledgement

Python `combinations` module.

```python
l = combinations(nums, k)
# nums should be a iterable object, k is the length of combination
# and it will return a iterable object
```
