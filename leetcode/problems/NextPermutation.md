## Approach

[Problem link](https://leetcode.com/problems/next-permutation/)

This is the first timt(maybe?) that my idea perfectly matches the offical approach.

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            # If a number is larger than it'f front number,there is something we can do
            if nums[n-i-1] > nums[n-i-2]:
                # If they are the last two numbers, just change them
                if i == 0:
                    nums[-1], nums[-2] = nums[-2], nums[-1]
                    return
                # If they are not the last two numbers
                else:
                    front = nums[n-i-2]   # record the front number
                    # Set a dictionary to store the index of nums
                    d = {}
                    for index, value in enumerate(nums[n-i-1:]):
                        d[value] = index
                    # Set a sorted lis 'l' to find the next larger number than front
                    l = list(d.keys())
                    l.sort()

                    # We should find the next larger number than the 'front' number nums[n-i-2],
                    # change them, and sort the rest list, just like the answer of [3,2,5,4,3,2,1]
                    # is [3,3,1,2,2,4,5] (something happened at '[2,5]')

                    # Find the number larger than 'front', then change
                    # this number and 'front' in nums
                    for k in range(len(l)):
                        if l[k] > front:
                            change_i = k
                            break
                    # Find index of the number to change
                    target_i = d[l[change_i]]
                    # Change them
                    nums[n-i-2], nums[target_i+n-i-1] = nums[target_i+n-i-1], nums[n-i-2]

                    # Sort the rest
                    for j in range((i+1)//2):
                        nums[n-i-1+j], nums[n-1-j] = nums[n-1-j], nums[n-i-1+j]
                    return
        nums.sort()
        # pass
```

As the comment, to deal with this problem, we should traverse the list from right to left, until finding a pair of number that 
`nums[i-1] < nums[i]`, and then find the next larger number in nums[i:], then swap the 'next-larger-number' and nums[i-1], then 
sort the new n[i:] with ascending order. And that's the result.

## Knowledge

- Lexicographically next greater permutation of numbers
In chinese, it means '字典序全排列'. For example, give a list `123`, it's lexicographically permutation is:
`123、132、213、231、312、321`,and it must be in this order.
