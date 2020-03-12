## Approach

[Problem link](https://leetcode.com/problems/unique-binary-search-trees/)

- My approach

Firstly I want use the method like [Unique Binary Search Trees 2](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/UniqueBinarySearchTrees2.md), 
(I don't understand why Unique Binary Search Trees 2 is 95 and 
Unique Binary Search Trees is 96), but it's time exceeded.

And after searching other's approach, I found there is a regular pattern of BST.

- Other's approach

```python
class Solution:
    def numTrees(self, n: int) -> int:
        
        memo = collections.defaultdict(int)
        
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        
        for i in range(3, n+1):
            for j in range(i):
                # Current number equals to the sum of the product of two numbers which sum equals to (n-1)
                memo[i] += memo[j]*memo[i-j-1]
        return memo[n]
```
