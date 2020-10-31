## 395. Longest Substring with At Least K Repeating Characters

[Problem link](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

- My approach

Use the method of `divide and conquer`. Find the characters which count is smaller than k, and divide the string at these characters. Then do the same operation of the 
substrings until find a substring that all the counts of characters are no less than k.

For example:

```
s = "aabcbd", k = 2

the count of c and d are smaller than k, so we divide the string at c and d: ["aab", "b"], and go on for these substrings.
```

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.res = 0
        
        def helper(st):
            # Find the small-count characters
            dic = {}
            for i in st:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
            notEnough = set()
            for j in dic:
                if dic[j] < k:
                    notEnough.add(j)
                  
            if not notEnough:
                self.res = max(self.res, len(st))
                return
            else:
                t = 0
                start = 0
                while t < len(st):  # divide the string
                    if st[t] in notEnough and start >= 0:
                        helper(st[start:t])
                        t += 1
                        start = -1
                    else:
                        if start < 0:
                            start = t
                        t += 1
                if start > 0:
                    helper(st[start:])
                    
        helper(s)
        return self.res
```

- Slide Window

The [official solution](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/) provides a slide window method.
