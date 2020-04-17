## Approach

[Problem link](https://leetcode.com/problems/palindrome-partitioning-ii/)

- My solution

My own solution failed. 

Then inspired by other's approach, found a dynamic method.

The method can be divide into two parts:

Firstly, use the method like [Palidrome Partitioning](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/PalidromePartitioning.md) create a dictionary `dicOfPali` to save the palindrome indexs.

Secondly, create a list `dp` do dynamic program, that dp[i] stands for minimum cuts of `s[:i]`.

```python
class Solution:
    def minCut(self, s: str) -> int:
        dicOfLetter = defaultdict(list)
        dicOfPali = defaultdict(list)
        # dicOfPali is a dictionary which key is index of s, and value is a list of indexs which can compose a palindrome with its key
        for i in range(len(s)):
            dicOfLetter[s[i]].append(i)
            for j in dicOfLetter[s[i]]:
                if s[j:i+1] == s[j:i+1][::-1]:
                    dicOfPali[min(i, j)].append(max(i, j))

        dp = [0] + [float('inf')]*len(s)
        for i in range(len(dp)):
            for l in dicOfPali[i]:
                # s[i:l+1] is a palindrome
                # So the minimum cuts of s[:l+1] equals to minimum cuts of s[:i] plus 1, and take the minimus value
                dp[l+1] = min(dp[l+1], dp[i] + 1)
        return dp[-1] - 1
```

For the method to create `dicOfPali`, because every time need to check if s[j:i+1] is a palindrome, it may run slowly. 

There is a improved method.

- Other's approach

```python
class Solution:
    def minCut(self, s: str) -> int:
        dicOfPali = collections.defaultdict(list)
        def expand(l, r):
            # Find palindrome from middle to edge
            while l >= 0 and r < len(s) and s[l] == s[r]:
                dicOfPali[l].append(r)
                l, r = l-1, r+1
        for i in range(len(s)):
            expand(i, i)
        for i in range(len(s) - 1):
            expand(i, i+1)
        
        # The following content is all the same
        dp = [0] + [float('inf') for _ in range(len(s))]
        for i in range(len(dp)):
            for l in dicOfPali[i]:
                dp[l+1] = min(dp[l+1], dp[i] + 1)
        return dp[-1] - 1
```

This method can run more faster.
