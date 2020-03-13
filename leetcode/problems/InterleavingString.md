## Approach

[Problem link](https://leetcode.com/problems/interleaving-string/)

- My approach

Use recursing method, check if the first letter in s3 equals to thhe first letter in s1 or s2, and do the same for their slices.

And by the prompt of official solution, use memory and set a tuple of three indexs(s1.index, s2.indx, s3.index) as key.

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.mem = {}
        def traceback(a, b, c):
            if c == len(s3):
                return True
            if a == len(s1):
                return s2[b:] == s3[c:]
            if b == len(s2):
                return s1[a:] == s3[c:]
            # Use a memory
            if (a, b, c) in self.mem:
                return self.mem[(a, b, c)]
            # There can be 4 situations:
            # 1.Neither s1 nor s2 is matched
            if s1[a] != s3[c] and s2[b] != s3[c]:
                return False
            # 2.Both s1 and s2 are matched
            elif s1[a] == s3[c] and s2[b] == s3[c]:
                self.mem[(a, b, c)] = (traceback(a+1, b, c+1) or traceback(a, b+1, c+1))
                return self.mem[(a, b, c)]
            # 3.s1 is matched and s2 is not
            elif s1[a] == s3[c] and s2[b] != s3[c]:
                self.mem[(a, b, c)] = traceback(a+1, b, c+1)
                return self.mem[(a, b, c)]
            # 4.s2 is matched and s1 is not
            elif s1[a] != s3[c] and s2[b] == s3[c]:
                self.mem[(a, b, c)] = traceback(a, b+1, c+1)
                return self.mem[(a, b, c)]
        if len(s1) + len(s2) != len(s3):
            return False
        return traceback(0, 0, 0)
```

And there is also a dynamic program method.

For more imformation of dp method, you can read the official solution.

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        m = len(s1) + 1
        n = len(s2) + 1
        # dp is a two-dimensional array, and dp[m-1][n-1] will be the final answer
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        for i in range(1, n):
            if dp[0][i-1] and s2[i-1] == s3[i-1]:
                dp[0][i] = True
        # If the left or above element is True, means current index of s3(i+j-1) can be reached, and at this situation if
        # current letter of s1(s1[i-1]) or s2(s2[j-1]) equals to s3[i+j-1], means current letter in s3 is available, set it to True.
        # Pay attention theat one letter can only be used once, so s1[i-1] should be paired with the above element(dp[i-1][j]),
        # and s2[j-1] should be paired with the left element(dp[i][j-1])
        for i in range(1, m):
            for j in range(len(dp[0])):
                if (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1]):
                    dp[i][j] = True
        return dp[m-1][n-1]
```
