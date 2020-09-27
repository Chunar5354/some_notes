## 354. Russian Doll Envelopes

[Problem link](https://leetcode.com/problems/russian-doll-envelopes/)

- My approach

My idea is sorting the array firstly, then use dynamic programming for every current envlope, check the envelopes before it.

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        dp = [1] * len(envelopes)
        envelopes.sort()
        for i in range(1, len(envelopes)):
            env = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    env = max(dp[j]+1, env)
            dp[i] = env
        return max(dp)
```

This method has O(n^2) time complexity, and it was time limit exceeded.

- Other's approach

The key idea is sorting the array as weight ascending and hight descending order. Then use binary search tree to find the position to insert envelopes by height. 
Because height is sorted in decending order, so at last we will find the smallest envelope for the same weight.

```python
class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: (x[0], -x[1]))
        tails = [inf] * len(A)
        size = 0
        for w in map(lambda x: x[1], A):
            i = bisect_left(tails, w)
            tails[i] = w
            size = max(i + 1, size)
        return size
```

[Here](https://leetcode.com/problems/russian-doll-envelopes/discuss/778932/Python-10-line-O(nlogn)-Binary-Search-(smallest-tail-of-increasing-subsequences)) is the link of this solution.

