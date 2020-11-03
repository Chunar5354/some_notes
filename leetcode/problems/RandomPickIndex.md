## 398. Random Pick Index

[Problem link](https://leetcode.com/problems/random-pick-index/)

- My approach

Save indexes of same value in a dictionary. And find randomly in dic[target].

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for idx, val in enumerate(nums):
            if val in self.dic:
                self.dic[val].append(idx)
            else:
                self.dic[val] = [idx]

    def pick(self, target: int) -> int:
        l = self.dic[target][:]
        for i in range(1, len(l)):
            p = 1/(i+1)
            n = random.random()
            if n > p:
                l[i] = l[i-1]
        return l[-1]
```

And this can be improved. Just traverse the array and when meet a target number, calculate the probability to ckeck if modify the answer. So we don't need the extra dictionary.

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        last_idx = 0
        res = 0
        for idx, val in enumerate(self.nums):
            if val == target:
                count += 1
                p = 1 / count
                n = random.random()
                if n > p:  # if random number is larger than current probability, modify it with the last result
                    res = last_idx
                else:
                    res = idx
                    last_idx = idx
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
