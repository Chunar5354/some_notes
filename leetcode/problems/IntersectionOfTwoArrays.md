## 349. Intersection of Two Arrays

[Problem link](https://leetcode.com/problems/intersection-of-two-arrays/)

- My approach

Translate the lists into collections, then return their intersection.

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```
