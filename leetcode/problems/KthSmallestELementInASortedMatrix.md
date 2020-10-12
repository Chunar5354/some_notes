## 378. Kth Smallest Element in a Sorted Matrix

[Problem link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

- Other's approach

The key point is how to find how many numbers smaller than target number in a 2D array.

```python
class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        
        while lo < hi:
            print(lo, hi)
            mid = (lo+hi) // 2
			
			      # saddleback search
            p, q, c = n-1, 0, 0 #(p,q) moving point, c: count
            while 0 <= p and q < n:
                if matrix[p][q] > mid:
                    p -= 1
                else:
                    c += p + 1 # how many numbers not larger than mid in qth column
                    q += 1
                    
            # binary search
            if c < k:
                lo = mid + 1
            else:
                hi = mid
            
        return lo
```
