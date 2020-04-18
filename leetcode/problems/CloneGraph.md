## Approach

[Problem link](https://leetcode.com/problems/clone-graph/)

- My approach

Firstly I was confused by graph. Because when I create a new node, there is a problem that I should fill its `neighbors`, and the nodes 
is `neighbors` also have `neighbors` need to be filled, it seems like a unlimited cycle.

And the key point to solve this problem is that we can create the nodes firstly, then fill them step by step.

I wrote a very complex code:

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # Firstly save all the values in dic
        dic = {}
        stack = [node]
        while stack:
            n = stack.pop()
            n_list = []
            for nd in n.neighbors:
                n_list.append(nd.val)
                if nd.val not in dic.keys():
                    stack.append(nd)
            dic[n.val] = n_list
        visited = []
        # The save all the new nodes in dic_n
        dic_n = {}
        for i in dic.keys():
            dic_n[i] = Node(i, [])
        # Finally fill the neighbor of every node
        stack = [dic_n[1]]
        visited = []
        while stack:
            crt_n = stack.pop()
            if crt_n.val not in visited:
                visited.append(crt_n.val)
                for i in dic[crt_n.val]:
                    stack.append(dic_n[i])
                    crt_n.neighbors.append(dic_n[i])
        return dic_n[1]
```

But there is no need to do there complex operation. We can create new nodes at first as the method below.

- Other's approach

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None    
        stack = [node]
        hm = {}
        # The key is given nodes, and the value is the copied new nodes
        hm[node] = Node(node.val)
        
        while stack:
            cur = stack.pop()      
            for nei in cur.neighbors:         
                if nei not in hm:
                    hm[nei] = Node(nei.val)    
                    stack.append(nei)             
                # append the copy of nei thru hm
                hm[cur].neighbors.append(hm[nei])
            
        return hm[node]
```
