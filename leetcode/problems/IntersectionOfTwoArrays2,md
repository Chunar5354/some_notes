## 350. Intersection of Two Arrays II

[Problem link](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

- My approach

Save one number list into dictionary as {value: count}. Then traverse the second number list, if n in dictionary, add current n in result and reduce its count, 
if the count of a number is 0, delete it from dictionary.

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for n in nums1:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        res = []
        for n in nums2:
            if n in dic:
                res.append(n)
                dic[n] -= 1
                if dic[n] == 0:
                    dic.pop(n)
        
        return res
```
