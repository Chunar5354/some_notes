## Approach

[Problem link](https://leetcode.com/problems/largest-number/)

- My approach

The key point of this problem is how to specify the sorting rules. To make the result is the largest number, we must ensure that 
every combination of two numbers is the largest, it can be expressed as `str(nums[i] + nums[i-1]) > str(nums[i-1] + nums[i])`.

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Firstly translate nums into string type
        nums = [str(n) for n in nums]
        
        for i in range(len(nums)):
            while i:
                if nums[i] + nums[i-1] > nums[i-1] + nums[i]:
                    nums[i], nums[i-1] = nums[i-1], nums[i] #swap
                else:
                    break
                i -= 1
                
        res = ''.join(nums)
        if res[0] == '0':
            return '0'
        return res
```

And to customize the sorting rule, we can use Python method `sorted(key=a_class)`.

By adding a parameter `key` to sorted funciton, we can customize the sorting rule as the value of key.

There are two ways to do this:

  - 1. Create a new class and overload the operator `<`(__lt__, less than).
  
  ```python
  class LargerNumKey(str):
      def __lt__(x, y):
          # We return the value as 'x+y > y+x', the result will be in descending order
          return x+y > y+x
        
  class Solution:
      def largestNumber(self, nums):
          largest_num = sorted(map(str, nums), key=LargerNumKey)
        
          largest_num = ''.join(largest_num)
          return '0' if largest_num[0] == '0' else largest_num
  ```
  
  2. Create a new function, and use Python build-in method cmp_to_key.
  
  ```python
  from functools import cmp_to_key
  class Solution:
      def largestNumber(self, nums: List[int]) -> str:
          # Atttention, to make the result is in descending order, the return value here is:
          # 'x + y < y + x returns 1', it's different from the method above
          cmp = lambda x, y: 1 if x + y < y + x else -1
          nums = list(map(str, nums))
          # Use cmp_to_key here
          nums.sort(key = cmp_to_key(cmp))
        
          res = int(''.join(nums))
          return str(res)
  ```
  
  For more details about `sorted()`, please see [here](https://docs.python.org/zh-cn/3/howto/sorting.html).
  
  And for more detaild about `cmp_to_key`, please see [here](https://zhuanlan.zhihu.com/p/26546486).
