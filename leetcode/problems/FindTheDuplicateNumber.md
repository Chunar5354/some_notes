## 287. Find the Duplicate Number

[Problem link](https://leetcode.com/problems/find-the-duplicate-number/)

- My approach

Because the question asks to solve the problem in O(1) space somplex and less than O(n^2) time complex, I didn't find out the answer.

- Official solution

Use the same method of [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Tortoise and the Hare）.

Think the array as a linked list, nums[i] means i.next.

```python
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
```

For more explinations, please see the [official solition](https://leetcode.com/problems/find-the-duplicate-number/solution/)
