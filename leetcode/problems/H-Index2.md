## 275. H-Index II

[Problem link](https://leetcode.com/problems/h-index-ii/)

- My approach

This problem is the same as [H-Index](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/H-Index.md), and the citations is sorted before. So we can use the same method.

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        for i in range(l):
            if citations[i] >= l-i:
                return l-i
        return 0
```
