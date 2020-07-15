## 229.Majority Element 2

[Problem link](https://leetcode.com/problems/majority-element-ii/)

- My approach

Sort the array and when `nums[i] != nums[i-1]` compare the count of nums[i-1] with len(nums)/3.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        nums += ['#']  # add an end symbol
        res = []
        start = 0
        
        for i in range(1, l+1):
            if nums[i] != nums[i-1]:
                curr = i - start
                if curr > l / 3:
                    res.append(nums[start])
                start = i
        return res
```

- Other's approach

Since the count majority element is larger than len(nums)/3, there can be at most 2 majority elements.

So we can create two varaibles and count them.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, count1, count2 = 0, 0, 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            # If any of the condition above are not satisfied, decrease the counts
            else:
                count1 -= 1
                count2 -= 1
        return [i for i in set((cand1, cand2)) if nums.count(i) > len(nums)/3]
```
