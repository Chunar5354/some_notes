## 409. Longest Palindrome

[Problem link](https://leetcode.com/problems/longest-palindrome/)

- My approach

All the numbers with even count can form in palindrome, and for the odd counts, we add count-1 into palindrome expect the max count(it can be at center).

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        res = 0
        longestOdd = 0
        for k in dic:
            if dic[k] % 2 == 0:
                res += dic[k]
            else:
                if dic[k] > longestOdd:
                    if longestOdd > 0:
                        res += (longestOdd-1)
                    longestOdd = dic[k]
                else:
                    res += dic[k]-1
        
        return res + longestOdd
```

- Official solution

There is a simplified version. If the current result is even and meet an odd count, this number with odd count can all be added.

```python
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
```
