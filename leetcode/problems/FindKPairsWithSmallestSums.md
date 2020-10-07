## 373. Find K Pairs with Smallest Sums

[Problem link](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

- My approach

Save all the pairs in to a list then sort them by their sum.

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append([nums1[i], nums2[j]])
        
        res.sort(key=sum)
        
        return res[:k]
```

- Other's approach

Use heap to sort them while adding pairs. The elements to sort is smaller than k, so this method can run faster.

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if nums1 == [] or nums2 == []:
            return []
        
        heap = []
        for j in range(len(nums2)):
            heapq.heappush(heap, (nums1[0]+nums2[j], (0, j)))

        result = []
        while len(result) < k and len(heap) > 0:
            # Every time append one line and only pop one pair
            curr = heapq.heappop(heap)
            result.append([nums1[curr[1][0]], nums2[curr[1][1]]])
            if curr[1][0]+1 < len(nums1):
                i = curr[1][0]+1
                j = curr[1][1]
                heapq.heappush(heap, (nums1[i]+nums2[j], (i, j)))
        
        return result
```
