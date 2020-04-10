## Approach

[Problem link](https://leetcode.com/problems/valid-palindrome/)

- My approach

To avoid the characters which are not numbers or alphabets, translate the characters into ASCII code and check if they are in valid area.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for c in s:
            # Check ASCII code
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                # Avoid cases
                stack.append(c.lower())
        return stack == stack[::-1]
```
