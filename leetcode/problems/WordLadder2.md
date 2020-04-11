## Approach

[Problem link](https://leetcode.com/problems/word-ladder-ii/)

- My approach

Check every word if it has only one different position from the last word, until go to endWord.

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        res = []
        # Check if two words have only one different position
        def checkDiff(s1, s2):
            num = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    num += 1
            return num
        
        def helper(wList, crt_res):
            if crt_res[-1] == endWord:
                res.append(crt_res)
                return
            if not wList:
                return
            for i in range(len(wList)):
                diffNum = checkDiff(wList[i], crt_res[-1])
                if diffNum == 1:
                    helper(wList[:i]+wList[i+1:], crt_res+[wList[i]])
                    
        helper(wordList, [beginWord])
        # Get the shorest answer in res
        minLength = float('inf')
        for r in res:
            minLength = min(len(r), minLength)
        return [r for r in res if len(r)==minLength]
```

This method need to check every word in every level, the time complex is `n!`. It's time exceeded.

But other's approaches are too complex, I will find another time to finish this problem.
