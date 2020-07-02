## Approach

[Problem link](https://leetcode.com/problems/contains-duplicate/)

- My approach

Traverse nums and save numbers in a collection, when meet a number that already in the collection, return True.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for n in nums:
            if n in mem:
                return True
            mem.add(n)
        return False
```

In Python, we can translate the given list into a collection, and if there are some duplications, their length will be different.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```
