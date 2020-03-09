## Approach

[Problem link](https://leetcode.com/problems/restore-ip-addresses/)

- My approach

Recursing method.

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        def traceback(prev, i, num):
            '''
            :prev: finished part of one IP address
            :i: current index of s
            :num: the number of '.' in prev
            '''
            if i >= len(s):
                if num == 4:
                    # Remove the last '.' in prev
                    self.res += [prev[:-1]]
                return
            if num == 4 and i < len(s):
                return
            if s[i] == '0':
                # There can't be any other number after '0' in one field
                traceback(prev+s[i:i+1]+'.', i+1, num+1)
                return
            j = 1
            while i+j <= len(s) and int(s[i:i+j]) <= 255:
                traceback(prev+s[i:i+j]+'.', i+j, num+1)
                j += 1
        traceback('', 0, 0)
        return self.res             
```
