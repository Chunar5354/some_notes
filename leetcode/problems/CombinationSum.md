## Approach

[Problem link](https://leetcode.com/problems/combination-sum/)

- My approach

Also a recursing method.
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Firstly, sort the list
        candidates.sort()
        res = []
        
        def subSum(l, t, sub_res):
            for i in range(len(l)):
                n = t - l[i]
                # n == 0 means find a result, append it into res
                if n == 0:
                    sub_res.append(l[i])
                    # Because 'append()' is a in-place method, here I make a copy of sub_res,
                    # or next operation for sub_res will change res
                    res_app = sub_res[:]
                    # Check if current res_app has already existed
                    res_app.sort()
                    if res_app not in res:
                        res.append(res_app)
                    # After add sub_res to res, we need to revert sub_res, 
                    # such as in this layer, sub_res is [2, 2, 2] at the begining, target is 8,
                    # so we add [2, 2, 2, 2] into res. But when the program is going on, 
                    # is must start with [2, 2, 2], not the result [2, 2, 2, 2]. 
                    # So we need to pop the last element which we added just now.
                    sub_res.pop(-1)
                # If n > 0, means the program can go further
                elif n > 0:
                    sub_res.append(l[i])
                    subSum(l, n, sub_res)
                    sub_res.pop(-1)
                else:
                    break
        subSum(candidates, target, [])
        return res
```

This code works, but it has some excess operation. And we can improve it.

- Optimized approach
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # Functions build in a class can't see the local variable here, 
        # so change it into self.res
        self.res = []
        
        def subSum(l, t, sub_res):
            for i in range(len(l)):
                n = t - l[i]
                if n == 0:
                    # Instead of using in-place method 'append()', simplely use '+' for list,
                    # so we don't need to create a copy or do 'pop()'
                    self.res += [sub_res+[l[i]]]
                elif n > 0:
                    # Pay attention to the 'l[i:]', 
                    # for next layer program, we just need to start traversing at current element,
                    # that can save time, and avoid duplication.
                    subSum(l[i:], n, sub_res+[l[i]])
                else:
                    break
        subSum(candidates, target, [])
        return self.res             
```

## Knowledge

- 1.`append()` is an in-place method, be careful when using it. You can use '+' for list instead.

- 2.Common function(without 'self') created in class can't see the class's local variable.
