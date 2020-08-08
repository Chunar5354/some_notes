## 278. First Bad Version

[Problem link](https://leetcode.com/problems/first-bad-version/)

- My aproach

The idea is using binary search.

Recursing method:

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(l, r):
            curr = (l+r)//2
            if isBadVersion(curr):
                # If the last version is not bad, the first bad version will be at left
                if not isBadVersion(curr-1):
                    return curr
                else:
                    return helper(l, curr)
            else:
                # If the next version is bad, the first bad version will be at right
                if isBadVersion(curr+1):
                    return curr+1
                else:
                    return helper(curr, r)
        return helper(0, n)
```

And iterable method:

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l+r)//2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l
```
