## 399. Evaluate Division

[Problem libk](https://leetcode.com/problems/evaluate-division/)

- Other's approach

We can see the structure as a directed graph, and the nodes are the characters in equations, the lines are the quotient fron head to tail.

Then we can do DFS for this graph, if the two nodes are not connected, return -1.

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = collections.defaultdict(dict)
        for i in range(len(equations)):
            dic[equations[i][0]][equations[i][1]] = values[i]
            dic[equations[i][1]][equations[i][0]] = 1 / values[i]

        def helper(x, y, visited):
            if x not in dic and y not in dic:
                return -1
            if y in dic[x]:
                return dic[x][y]
            for i in dic[x]:
                if i not in visited:
                    visited.add(i)
                    # we want to get the result of x->y, if y is not connect directly with x, find deeperly
                    curr = helper(i, y, visited)
                    if curr == -1:
                        continue  # find next
                    return dic[x][i] * curr
            return -1
        
        res = []
        for a, b in queries:
            res.append(helper(a, b, set()))
        
        return res
```
