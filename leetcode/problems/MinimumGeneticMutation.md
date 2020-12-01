## 433. Minimum Genetic Mutation

[Problem link](https://leetcode.com/problems/minimum-genetic-mutation/)

- My approach

Each mutation can only change one character, so we can search from the bank if there is a string that has only onr different character from current 'start' string, if there is, 
modify the string to 'start', and go on search until finding the 'end' string.

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        def hasOneDiff(a, b):  # check if the two strings have only one different character
            diff = 0
            for j in range(len(a)):
                if a[j] != b[j]:
                    diff += 1
            return diff == 1
        
        self.res = float('inf')
        def helper(target, cand, count):
            if target == end:
                self.res = min(count, self.res)
            for i in range(len(cand)):
                if hasOneDiff(target, cand[i]):
                    helper(cand[i], cand[:i]+cand[i+1:], count+1)
        
        helper(start, bank, 0)
        if self.res == float('inf'):
            return -1
        return self.res
```
