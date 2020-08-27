## 310. Minimum Height Trees

[Problem link](https://leetcode.com/problems/minimum-height-trees/)

- My approach

My idea is using recursing to find the height of all the possible tree, and return the minimum, but it was time limited exceeded.

- Other's approach

We can notice that the root of trees with minimum height must in the middle. Or we can see in the graph, it must have more than one connections. So we can start from the leaves, 
every time cut on leaf until there are all leaf nodes, the remained nodes are the root of minimum trees.

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        connections = defaultdict(set)
        for x, y in edges:
            connections[x].add(y)
            connections[y].add(x)
            
        leaves = [x for x in range(n) if len(connections[x]) == 1]
        while leaves and len(leaves) < len(connections):
            new = []
            for x in leaves:
                for y in connections[x]:
                    connections[y].remove(x)  # cut leaves
                    if len(connections[y]) == 1:  # current node may become a new leaf
                        new.append(y)
                connections.pop(x)  # remove leaf nodes
            leaves = new
        return list(connections)
```
