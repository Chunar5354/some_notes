## Approach

[Problem link](https://leetcode.com/problems/merge-sorted-array/)

- My approach

Just compare the elements in nums1 and nums2, and add nums2 into nums1. But pay attention to the limit of length.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for j in range(n):
            # Skip the elements which are smaller than current nums2[j]
            while nums1[i] <= nums2[j] and i < m+j:
                i += 1
            # Firstly move the next (m+j-i) elements of current nums1[i], then add nums2[j] into nums1[i]
            for k in range(m+j-i):
                nums1[m+j-k] = nums1[m+j-k-1]
            nums1[i] = nums2[j]
```

This method is not very clearly, I found an other's method which is more clearly.

- Other's approach

This approach adds the elements from right to left, so it can avoid the moving operations.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            # We only need to deal with the first m elements in nums1, and first n elements in nums2
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
```
