## Approach

[Problem link](https://leetcode.com/problems/subsets/)

- My approach

Firstly I want to use resursing method.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def traceback(sub_n):
            if sub_n not in self.res:
                self.res.append(sub_n)
            for i in range(len(sub_n)):
                traceback(sub_n[:i]+sub_n[i+1:])
        traceback(nums)
        return self.res
```

But it's time limit exceeded.

And then I found a non recursing method, by reducing the numbers one by one.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_sub(l):
            # Every time get the list after reducing one number
            sub_ans = []
            for sub_l in l:
                for i in range(len(sub_l)):
                    sub_l_after = sub_l[:i] + sub_l[i+1:]
                    if sub_l_after not in sub_ans:
                        sub_ans.append(sub_l_after)
            return sub_ans
        sub_res = [nums]
        res = [[]]
        while len(sub_res[0]) > 0:
            res += sub_res
            sub_res = get_sub(sub_res)
        return res
```

- Other's approach

There is a very easy method.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            # Every time add current number to the existed answers
            res += [i+[num] for i in res]
            print(res)
        return res
```
