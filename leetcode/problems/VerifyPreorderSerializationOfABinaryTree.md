## 331. Verify Preorder Serialization of a Binary Tree

[Problem link](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)

- Other's approach

Imagine that every node needs a slot to settle, and when there comes a null node, it will take one slot, when there comes a non-null node, it take one slot and bring two new slots.

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p = preorder.split(',')
        
        # initially we have one empty slot to put the root in it
        slot = 1
        for node in p:
            
            # no empty slot to put the current node
            if slot == 0:
                return False
                
            # a null node?
            if node == '#':
                # take one slot
                slot -= 1
            else:
                # take one and bring two
                slot += 1
        
        # at last we don't allow any empty slot
        return slot==0
```
