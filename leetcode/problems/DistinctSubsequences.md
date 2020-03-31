## Approach

[Problem link](https://leetcode.com/problems/distinct-subsequences/)

- My approach

Firstly I want to use recursing method, but it's time limit exceeded.

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dic = {}
        for idx, val in enumerate(s):
            if val in t:
                if val not in dic:
                    dic[val] = [idx]
                else:
                    dic[val].append(idx)
        if set(dic.keys()) != set(t):
            return 0
        
        def helper(index, lastIndex):
            if index == len(t):
                return 1
            ways = 0
            # print('t[i] is: {}, lastIndex is: {}'.format(t[index], lastIndex))
            for i in dic[t[index]]:
                if i > lastIndex:
                    # Only current index larger than the index of last character can compose a way
                    crt_ways = helper(index+1, i)
                    ways += crt_ways
            return ways
        
        res = 0
        for i in dic[t[0]]:
            crt_res = helper(1, i)
            res += crt_res
        return res
```

Then I found a dynamic method from others.

- Other's approach

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]  #dp[m+1][n+1] means s[:m+2] t[:n+2]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]  # drop s[i]
        return dp[-1][-1]
```

To explain this method, give an example. 

```
s = 'bagbgbag'
t = 'bag'

Finally, dp is like this:

0, 0, b, a, g
0, 1, 0, 0, 0
b, 1, 1, 0, 0
a, 1, 1, 1, 0
g, 1, 1, 1, 1
b, 1, 2, 1, 1
g, 1, 2, 1, 2
b, 1, 3, 1, 2
a, 1, 3, 4, 2   # This row
g, 1, 3, 4, 6

The first row and first column stands for t and s
```

So dp[i][j] stands for the number of distinct subsequences of s[:i] and t[:j].

Traverse dp, if current s[i] == t[j], then dp[i][j] = dp[i-1][j] + dp[i-1][j-1], or dp[i][j] = dp[i-1][j].

Because dp[i-1][j] stands for the number of the distinct subsequecses of s[:i-1] and t[:j], and dp[i-1][j-1] stands for the number 
of the distinct subsequences of s[:i-1] and t[j-1].

For example, see the marked row above.
```
Now dp[7][2] => s[6] = t[1] = 'a'

So dp[6][2] stands for distinct subsequences of s[:6]('bagbgb') and t[:2]('ba') which equals to 1, 
and dp[6][1] stands for distinct subsequences of s[:6]('bagbgb') and t[:1]('b') which equals to 3.

So dp[7][2] stands for distinct subsequences of s[:7]('bagbgba') and t[:2]('ba') 
which equals to (t[:1] extends to t[:2]('ba') which there are 3 ways) plus (the already existed t[:2]('ba') which there is 1)
```
