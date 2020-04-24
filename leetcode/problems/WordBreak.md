## Approach

[Problem link](https://leetcode.com/problems/word-break/)

- My approach

Use recursing method, check if there is a prefix of s in wordDict. If yes, modify s as `s[len(w):]` and go on until `s = ''`.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        def helper(sub_s):
            # If self.res is True, means there is a valid answer. There is no need to do next operation
            if self.res:
                return
            if not sub_s:
                self.res = True
                return
            for w in wordDict:         
                if sub_s[:len(w)] == w:
                    # If there is a prefix of sub in wordDict, cut off all the duplicated 'w'
                    start = len(w)
                    while sub_s[start:start+len(w)] == w:
                        start += len(w)
                    helper(sub_s[start:])
        helper(s)
        return self.res
```

- Other's approach

The key point is also find the prefix. But instead cutting off the duplications, he use decorator `@lru_cache` as a memory.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def helper(s):
            if not s:
                return True
            for w in wordDict:
                if s[:len(w)] == w:
                    if helper(s[len(w):]):
                        return True
            return False
        return helper(s)   
```

- Knowledge

When use a recursing code, to save he running time, we can use `@lru_cache`(least recently used) as amemory.
