## Approach

[Problem link](https://leetcode.com/problems/palindrome-partitioning/)

- My approach

Create a dictionary to save the index of valid palindrome. Then use these palindromes filling the index of s from start to end.

```python
from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dicOfLetter = defaultdict(list)
        dicOfPali = defaultdict(list)
        # dicOfPali is a dictionary which key is index of s, and value is a list of indexs which can compose a palindrome with its key
        for i in range(len(s)):
            dicOfLetter[s[i]].append(i)
            for j in dicOfLetter[s[i]]:
                if s[j:i+1] == s[j:i+1][::-1]:
                    dicOfPali[min(i, j)].append(max(i, j))
        res = []
        def helper(idx, crt_res):
            if idx == len(s):
                res.append(crt_res)
                return
            # Every s[idx: end+1] now is a palindrome, and end+1 is the start of next palindrome, until the final element
            for end in dicOfPali[idx]:
                helper(end+1, crt_res+[s[idx:end+1]])
        helper(0, [])
        return res
```

  - Example

If the given `s` is "abcbaa", `dicOfPali` will be:
```python
{0: [0, 4], 1: [1, 3], 2: [2], 3: [3], 4: [4, 5], 5: [5]}
```

And there is a brief method from others.

- Other's approach

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def isPal(s):
            return s == s[::-1]
        
        def fn(s, l):
            if not s:
                ret.append(l)
                return
            # Traverse s, if current s[:i] is a palindrome, add s[:i] to result and go to traverse s[:i]
            for i in range(1, len(s)+1):
                if isPal(s[:i]):
                    fn(s[i:], l+[s[:i]])
        fn(s, [])
        return ret
```
