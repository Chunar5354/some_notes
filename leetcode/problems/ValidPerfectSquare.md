## 367. Valid Perfect Square

[Problem link](https://leetcode.com/problems/valid-perfect-square/)

- My approach

Use binary search, the max num is 2**31-1, ant the int(sqrt(2**31-1)) is 46340. So we start from 46340/2 to do binary search.

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = 46341
        
        m = (l+r) // 2
        last = m
        
        while True:
            if m * m == num:
                return True
            elif m * m < num:
                l = m
                m = (m+r) // 2
            else:
                r = m
                m = (l+m) // 2
            if last == m:
                return False
            last = m
```

Or we can start search at num//2.

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=0
        right=num
        while left<=right:
            mid=(left+right)//2
            square=mid*mid
            if square == num:
                return True
            elif square>num:
                right=mid-1
            else:
                left=mid+1
        return False
```
