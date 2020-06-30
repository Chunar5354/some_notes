## Approach

[Problem link](https://leetcode.com/problems/shortest-palindrome/)

- My approach

My idea is traverse from right to left, and check if s[:i] is a palindrome. This can find the longest palindrome from the beginning of s. Then the result is the reverse of `s[i:]+s`.

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # Find the longest palindrome s[:i]
        for i in range(len(s), -1, -1):
            idx = i
            if s[:i][::-1] == s[:i]:
                break

        return s[idx:][::-1]+s
```

- Official approach

There is a more faster method by using two pointers and recursing.

For the whole explination, please see [official solution](https://leetcode.com/problems/shortest-palindrome/solution/). And in my understanding, the key idea of this method is 
cutting the suffix which can't be in the palindrome every time until finding the longest palindrome start from beginning.

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in range(n-1, -1, -1):
            # Every time s[i] = s[j], increase i
            if s[i] == s[j]:
                i += 1
        if i == n:
            return s
        # remain_rev is the suffix that can't be in palindrome
        remain_rev = s[i:n][::-1]
        # Continue finding palindrome in s[:i]
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]
```

There is another method using `KMP`(Knuth–Morris–Pratt) algorithm, but it's a little complex.

For more details about this approach, please see official solution. And for more explinations about `KMP`, please see this [blog](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)
