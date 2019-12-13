## Approach

[Problem link](https://leetcode.com/problems/wildcard-matching/)

- My approach

This is also a problem like `regular expression`. And there is a similar problem before: [Regular Expression Matching](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/RegularExpressionMatching.md)

Firstly I use a method like force solution, it needs to judge many situations, and I failed.

And inspired by other's approach, I find a solution. Th main idea is set '*' `matches empty '' firstly by default`.
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)
        si, pi = 0, 0
        last_star = -1
        s_match = -1
        while si < ls:
            if pi < lp and (p[pi] == s[si] or p[pi] == '?'):
                si += 1
                pi += 1
            # If p[pi] == '*', record index of '*' and index of current matched s: '
            # In this case, we default '*' matches empty string ''
            elif pi < lp and p[pi] == '*':
                last_star = pi
                s_match = si
                pi += 1
            # If there is a '*' before, restart the matching as si=s_match, pi=last_star
            # In this case, we set this '*' matches one more element(s_match+1) than the last string
            elif last_star != -1:
                si = s_match + 1
                pi = last_star + 1
                s_match += 1
            # Else means p[pi] is not '?' or '*' and there is no '*' before
            else:
                return False
        # There may be some elements remained in p, they must be all '*', or return False
        if pi < lp:
            for sub_p in p[pi:]:
                if sub_p != '*':
                    return False
        return True
```
