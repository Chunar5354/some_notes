## 332. Reconstruct Itinerary

[Problem link](https://leetcode.com/problems/reconstruct-itinerary/)

- My approach

I wanted to use map firstly.

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        for t in tickets:
            if t[0] in dic:
                dic[t[0]].append(t[1])
            else:
                dic[t[0]] = [t[1]]
        
        for k in dic:
            dic[k].sort()
            
        start = 'JFK'
        res = ['JFK']
        while start in dic and dic[start]:
            start = dic[start].pop(0)
            res.append(start)
        
        return res
```


But this method may loss some nodes.


- DFS

This problem is betterly solved by DFS method. FIrstly I was confused and thought this was a graph problem, and I was focus on if there is a circle in all the nodes.

But this problem can just fit DFS, if we use a recursing method to traverse all nodes, there will be no nodes lost.

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        for t in tickets:
            if t[0] in dic:
                dic[t[0]].append(t[1])
            else:
                dic[t[0]] = [t[1]]
        
        for k in dic:
            dic[k].sort()
            
        res = []
        def helper(start):
            while start in dic and dic[start]:
                next_start = dic[start].pop(0)
                helper(next_start)
            res.append(start)
            
        helper('JFK')
        return reversed(res)
```
