## 264. Ugly Number II

[Problem link](https://leetcode.com/problems/ugly-number-ii/)

- My approach

My idea is start from 1, add all the (num*2, num*3, num*5) into the array.

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = {1}
        last = {1}
        # Every time add (num*2, num*3, num*5) may skip some middle numbers
        # so we set the end condition with 4*n
        while len(s) < 4*n:
            curr = set()
            for num in last:
                curr |= {num*2, num*3, num*5}
            last = curr
            s |= curr
        res = list(s)
        # Sort the array and the nth element is the answer
        res.sort()
        return res[n-1]
```

We can see the list of ugly numbers is stable. For such situations we can create the list as a global variable, and the function just need to get the nth element.

```python
s = {1}
last = {1}
# The question description tells us n is less than 1690
while len(s) < 3*1690:
    curr = set()
    for num in last:
        curr |= {num*2, num*3, num*5}
    last = curr
    s |= curr
res = list(s)
res.sort()

class Solution:
    def nthUglyNumber(self, n):
        return res[n-1]
```

Because it doesn't need to create a list for every invoke, this code can run more faster.

- Other's approach

There is another way to create the ugly number list.

```python
nums = [1]
i2, i3, i5 = 0, 0, 0
for _ in range(1690):
    ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
    nums.append(ugly)
    if ugly == nums[i2] * 2: i2 += 1
    if ugly == nums[i3] * 3: i3 += 1
    if ugly == nums[i5] * 5: i5 += 1

class Solution:
    def nthUglyNumber(self, n):
        return nums[n - 1]
```
