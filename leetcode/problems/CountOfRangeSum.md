## 327. Count of Range Sum

[Problem link](https://leetcode.com/problems/count-of-range-sum/)

- My approach

O(n^2) method was time limited exceeded.

- Other's approach

[Here](https://leetcode.com/problems/count-of-range-sum/discuss/78016/Very-concise-solution-in-Python-with-explanation) is a method from others.

He changes sum(i, j) into `sum(0, j) - sum(0, i)`, and uses binary search tree to sort the sums.

```python
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix,thisSum,ans = [0],0,0
        # the elemens in prefix stands for sum(0, i) for every i < j, which j is current position
        for n in nums:
            thisSum += n
            # bisect_right and bisect_left return the index to insert thisSum-lower or thisSum-upper into prefix.
            # The different of them is how many available sums in this loop
            # We set x to stand for numbers in prefix, x < thisSum-lower equals to thisSum-x > lower, 
            # thisSum is sum(0, j), x is sum(0, i) so thisSum-x is sum(i, j), so as thisSum-upper
            ans += bisect.bisect_right(prefix, thisSum-lower) - bisect.bisect_left(prefix, thisSum-upper)
            bisect.insort(prefix, thisSum)
        return ans
```
