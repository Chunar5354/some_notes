## Approach

[Problem link](https://leetcode.com/problems/majority-element/)

- My approach

We can create a hashmap to store how many time a number appeared.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        l = len(nums)/2
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
            if d[i] > l:
                return i
```

And there is a more clear method.

- Official approach

We can sort the given array firstly, beacuse the majority element is more than len(nums)/2, so after sorting the array, the middle 
element must be the majority element.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
```
