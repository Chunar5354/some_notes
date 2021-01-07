## 468. Validate IP Address

[Problem link](https://leetcode.com/problems/validate-ip-address/)

- My approach

This is not a good question.

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip = IP.split('.')
        if len(ip) == 4:
            for i in ip:
                if not i:
                    return 'Neither'
                if i[0] == '0' and len(i) > 1:
                    return 'Neither'
                curr = 0
                for n in i:
                    if n not in '1234567890':
                        return 'Neither'
                    curr = curr*10 + int(n)
                print(curr)
                if curr > 255:
                    return 'Neither'
            return 'IPv4'

        else:
            ip = IP.split(':')
            if len(ip) == 8:
                for i in ip:
                    if not i or len(i) > 4:
                            return 'Neither'
                    for n in i:
                        if n not in '1234567890abcdefABCDEF':
                            return 'Neither'
                return 'IPv6'
            else:
                return 'Neither'
```
