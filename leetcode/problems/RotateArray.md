## Approach

[Problem link](https://leetcode.com/problems/rotate-array/)

- My approach

We can reverse the array firstly, then pop the first element and append it at the end. And do the same operation for k times.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        for i in range(k):
            to_append = nums.pop(0)
            nums.append(to_append)
        nums.reverse()
```

The official solution uses a smart method to swap the elements of k intervals. For more information, please see the official solution.
