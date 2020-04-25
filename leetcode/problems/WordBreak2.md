## Approach

[Problem link](https://leetcode.com/problems/word-break-ii/)

- My approach

My own approaches are time limited exceeded.

- Other's approach

There is a clear recursing method with memory.

The `memo` is used to store the possible combination of current string with words in `wordDict`.

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        
        def search(string):
            if string in memo:
                return memo[string]
            else:
                paths = []
                
                # base case
                # we include this in here in the case a word
                # that exists in the dictionary can be further decomposed
                if string in wordDict:
                    paths.append(string)
                
                for i in range(len(string)):
                    # if a prefix exists, then see if remainder can be decomposed
                    if string[:i] in wordDict:
                        path = search(string[i:])
                        # if it can't be decomposed, then it will be empty
                        # for each decomposition, prepend the prefix
                        for p in path:
                            paths.append(string[:i] + " " + p)

                memo[string] = paths
                return memo[string]
        
        return search(s)
```
