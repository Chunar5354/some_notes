## 260. Single Number III

[Problem link](https://leetcode.com/problems/single-number-iii/)

- My approach

Because all the other numbers appear twice, we can create a set and when meet the first number add it into set, when meet the twice number remove from the set. Finally 
there will be only the two target numbers remained in set.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums: 
            return None
        
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        
        return list(s)
```

- Other's approach

There is a method using `XOR`, and it's O(1) space complex.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0   
        for n in nums:
            mask ^= n
            
        diff = mask & -mask
        
        x = 0
        for n in nums:
            if n & diff:
                x ^= n
        
        return [x, x ^ mask]
```
