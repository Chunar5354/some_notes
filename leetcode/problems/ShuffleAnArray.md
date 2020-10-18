## 384. Shuffle an Array

[Problem link](https://leetcode.com/problems/shuffle-an-array/)

- My approach

Every time choose an element randomly, add it at the end of result, and delete it from the original array.

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.l = nums
        self.c = set(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.l
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        curr = self.c.copy()
        while curr:
            n = random.choice(list(curr))
            res.append(n)
            curr.remove(n)
        return res
```
