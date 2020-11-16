## 413. Arithmetic Slices

[Problem link](https://leetcode.com/problems/arithmetic-slices/)

- My approach

Traverse the array and find every longest same-difference subarray. The count of arthemetic slices can be calculated by the length of subarray.

For example:

```
If the length of subarray is 6, like [1, 2, 3, 4, 5, 6].

The length of arthemetic slice can be 6, 5, 4 and 3

for the length 6, there is only one slice [1, 2, 3, 4, 5, 6]

and for the length 5, there are two slices [1, 2, 3, 4, 5] and [2, 3, 4, 5, 6]

then for length 4, there are 3 slices, and for length 3, there are 4 slices.
```

So if the length of subarray is n, the count of arthemetic slices equals to `sum(i for i in (1, n+2)`.

```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        start = 0
        diff = A[1] - A[0]
        i = 1
        res = 0
        while i < len(A)-1:
            if A[i+1] - A[i] == diff:
                while i < len(A)-1 and A[i+1] - A[i] == diff:  # get the length of subarray
                    i += 1
                l = i - start + 1
                for j in range(1, l-3+2):
                    res += j  # add into result
                if i+2 < len(A):  # new start
                    start = i + 1
                    diff = A[i+2] - A[i+1]
                    i += 2
            else:
                start = i
                if i+1 < len(A):
                    diff = A[i+1] - A[i]
                i += 1
        return res
```
