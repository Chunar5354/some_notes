## 451. Sort Characters By Frequency

[Problem link](https://leetcode.com/problems/sort-characters-by-frequency/)

- My approach

Sort the characters by the count.

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        count = {}
        for k in dic:
            if dic[k] in count:
                count[dic[k]].append(k)
            else:
                count[dic[k]] = [k]
        
        counts = list(count.keys())
        counts.sort()
        res = ''
        for n in counts:
            for c in count[n]:
                res = n*c + res
        return res
```


In python, we can use `lambda` in sort.

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        res = ""
        count = list(dic.keys())
        count.sort(key = lambda x: -dic[x])
        for c in count:
            res += c * dic[c]
        return res
```
