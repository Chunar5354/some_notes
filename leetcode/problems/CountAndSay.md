## Approach

[Problem link](https://leetcode.com/problems/count-and-say/)

Finally I can write a recursing program. That's a big progress.

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        def giveAns(t, s):
            if t == n:
                return s
            count = 1
            sub_s = ''
            for i in range(len(s)):
                # If this is the last char, add to sub_s and go to next layer
                if i == len(s) - 1:
                    sub_s += (str(count) + s[i])
                    return giveAns(t+1, sub_s)
                if s[i+1] == s[i]:
                    count += 1
                else:
                    sub_s += (str(count) + s[i])
                    count = 1
        return giveAns(1, '1')
```

A good training of recursing.
