## Approach

[Problem link](https://leetcode.com/problems/kth-largest-element-in-an-array/)

- My approach

Just sort the given array and return the kth element from right.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
```

### Knowledgement

In Python, sort method uses `TimSort` algorithm, for more details about TimSort, please see [here](https://blog.csdn.net/yangzhongblog/article/details/8184707).

And for this problem, using `heap` can make the code faster. We can use the module `headq`:

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k, nums)
        
        return res[-1]
```

For more details about headq, please see [the document](https://docs.python.org/zh-cn/3/library/heapq.html)
