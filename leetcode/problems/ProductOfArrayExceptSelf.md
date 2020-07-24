## 238. Product of Array Except Self

[Problem link](https://leetcode.com/problems/product-of-array-except-self/)

- My approach

I didn't solve this problem by O(N) time complex, I used brout force and it didn't accept.

- Official solution

The official solution provided a good approach that use two arrays to solve the sub products.

For example:

```
The given array is [1, 2 ,3, 4], we create two arrays 'left' and 'right'.

left[i] stands for the product until i-1, so left will be [1, 1, 2, 6].

And right[i] stands for the product from right until i+1, so right will be [24, 12, 4, 1].

And the answer array res[i] = left[i] * right[i].
```

Here is the code:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1] * l
        for i in range(1, l):
            left[i] = left[i-1] * nums[i-1]
            
        right = [1] * l
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        res = [1] * l
        for i in range(l):
            res[i] = left[i] * right[i]
        return res
```

And the approach above can be improved. Because it uses two extra arrays. It can be solved by constant space complexity.

We change the left array to res array, and use a pointer 'R' to represent the 'right[i]' element.

The code will be:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        R = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = R * res[i]
            R *= nums[i]

        return res
```
