## Approach

[Problem link](https://leetcode.com/problems/copy-list-with-random-pointer/)

- My approach

The key point is how to find the random attribute of new node.

Use two dictionary, and linked the given node list and new node list with the index of node, here is `num`.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new_node = {None: None}
        node = {None: None}
        n = head
        num = 0
        # Both node and new_node have 'num', it stands for the index of every node
        while n:
            new_node[num] = Node(n.val)
            node[n] = num
            num += 1
            n = n.next
        new_node[num] = None
        i = 0
        while head:
            new_node[i].next = new_node[i+1]
            # Now we can find the index of current random node from 'node', and get new node from 'new_node' by index
            new_node[i].random = new_node[node[head.random]]
            i += 1
            head = head.next
        return new_node[0]
```

- Other's approach

There is a reursing method from other's. He use a memory `visited` to link the given node list and new node list.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def helper(node):
            if not node:
                return None
            # The value of visited is new node, and both its next and random attribute have already been modified here
            if node in visited:
                return visited[node]
            # If current node has not been visited, create a new node and add it into visited
            crt_node = Node(node.val)
            visited[node] = crt_node
            
            crt_node.next = helper(node.next)
            crt_node.random = helper(node.random)
            return crt_node
        return helper(head)     
```
