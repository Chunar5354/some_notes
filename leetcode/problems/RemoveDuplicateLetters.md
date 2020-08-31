## 316. Remove Duplicate Letters

[Problem link](https://leetcode.com/problems/remove-duplicate-letters/)

- My approach

My own idea was create a stack and a dictionary to store current sub string and when a new letter comes, check if it is already in current string and modify the string to minimum.

But it failed.

- Other's approach

There is an other's method which is close to mine. 

but he has a very smart idea which is using a `last_occurance` dictionary. By using this dictionary, we can check if current letter is in the remained part of s. So we can remove the 
letters and be not afraid of losing this letter.

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurance = {}
        for i in range(len(s)):
            last_occurance[s[i]] = i
        
        for i, ch in enumerate(s):
            if (ch in seen):
                continue
            else:
                # last_occurance[stack[-1]] > i can guarantee not lose current ch
                while (stack and stack[-1] > ch and last_occurance[stack[-1]] > i):
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                seen.add(ch)
                stack.append(ch)
        return ''.join(stack)
```
