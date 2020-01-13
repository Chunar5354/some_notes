## Approach

[Problem link](https://leetcode.com/problems/edit-distance/)

Firstly I had no idea, so I immediately search other's approaches.

Most of them used `dynamic program`. The main idea is: there are 3 operations(insert, delete, replace), and the number of current step 
equals to the `minimum` of these three opreations.

Here is one of the approaches
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}   # Set a dictionary to store results, it also can be a memory
        def dp(a,b): 
            # If get the start of any of the rowd:
            if a == -1 or b == -1:
                if b > -1:
                    # Means word2 is remained, need to do b+1 inserting
                    return b + 1
                if a > -1:
                    # Means word1 is remained, need to do a+1 deleting
                    return a + 1
                else:
                    return 0
            # Check the memory
            if (a,b) not in mem:
                # case 1: last character is a match
                if word1[a] == word2[b]:
                    mem[(a,b)] = dp(a - 1, b - 1)
                # case 2 3 4: no match. 
                else:
                    # insert
                    c_insert = dp(a, b - 1)
                    # delete
                    c_delete = dp(a - 1, b)
                    # replace
                    c_replace = dp(a - 1, b - 1)
                    cost = 1 + min(c_insert, c_delete, c_replace)
                    mem[(a,b)] = cost
            return mem[(a,b)]
        return dp(len(word1) - 1, len(word2) - 1)
```

And there is also a method without using explicit memory. It uses a decorator `lru_cache` to comply memory. 
[See more details here](https://zhuanlan.zhihu.com/p/27643991)
```python
from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i >= m:
                return n - j  # insert the rest of word2[j:]
            elif j >= n:
                return m - i  # delete the rest of word1[i:]
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
		    # replace, insert, delete, respectively
            return 1 + min(dp(i + 1, j + 1), dp(i, j + 1), dp(i + 1, j))
        
        m, n = map(len, (word1, word2))
        word1, word2 = map(list, (word1, word2))
        return dp(0, 0)
```

## Knowledge

- Decorator `lru_cache` can set a memory to recursing function, so it can save time.
```python
from functools import lru_cache

@lru_cache
def traceback():
    # do something
```
