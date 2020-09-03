## 321. Create Maximum Number

[Problem link](https://leetcode.com/problems/create-maximum-number/)

- Other's approach

There is a very smart method.

He divided the operation to 2 parts, firstly find i maximum numbers of nums1 and k-i maximum numbers of nums2, then get the maximum combination of them.

```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def prep(nums, k):
            '''
            Find k manimum numbers of nums in origin order
            '''
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            '''
            The maximum combination of a and b
            '''
            return [max(a, b).pop(0) for _ in a+b]


        res = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                res.append(merge(prep(nums1, i), prep(nums2, k-i)))
        return max(res)
```
