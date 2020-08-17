## 295. Find Median from Data Stream

[Problem link](https://leetcode.com/problems/find-median-from-data-stream/)

- My approach

The key point is how to keep the list sorted whild inserting data.

My idea is using binary insert.

```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.even = 1
        self.len = 0
        

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
        else:
            l = 0
            r = self.len
            i = (l+r) // 2
            while l < r:
                if self.nums[i] > num:
                    r = i
                else:
                    l = i + 1
                i = (l+r) // 2
            
            self.nums = self.nums[:i] + [num] + self.nums[i:]
                    
        self.even *= -1
        self.len += 1
        

    def findMedian(self) -> float:
        if self.even == 1:
            return (self.nums[self.len//2] + self.nums[self.len//2-1]) /2
        else:
            return float(self.nums[self.len//2])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

- Official solution

To sort the array dynamicly, `heap` is a good method.

```python
from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        # Every time add the smallest number from self.large to self.small
        # or add the larger number from self.small to self.large
        # so the median is (max(self.small)+min(self.large))/2 (even) or min(self.large) (odd)
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))  # Because python headq can only pop the smallest number, here we change it to opposite number
        else:
            heappush(self.small, -heappushpop(self.large, num))
        # print(self.small, self.large)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
```

Another way to keep the list sorted is `binary search tree`

In Python, there is a `binsect` module which provides binary search method.

```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)  # binsect.insort() can add num to self.l then sort it
        
    def findMedian(self) -> float:
        m,r = divmod(len(self.l), 2)
        if r: return self.l[m]
        elif m: return sum(self.l[m-1:m+1])/2
        return []
```
