## 440. K-th Smallest in Lexicographical Order

[Problem link](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)

- My approach

I wanteed to use the same method as [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/).

But it was time limited exceeded.

- Other's approach

The key point is counting how many available numbers can be cut by current position.

For example, give n = 120, k = 20.

```
First loop(current number is 1): find the available cut of '1' is 32(1~10, 100~120), 32 > k, means we can't cut all the numebrs start with '1', we need to go deeper, 
so mutiply current number with 10

Second loop(current number is 10）: find the available cut of '10' is 11(10, 100~109), 11 < k, means we can cut all the numbers start with '10', the we go broder

Third loop(current number is 11): find the available cut of '11' is 11(11, 110~119), 11 > k(k is 7 now), so go deeper

Forth loop(current number is 110): find the available cut of '110' is 1(110 only), 1 < k, fo broder

...

Go on this, and finally when k==0, we can find the target number
```

```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        cur = 1
        while k > 0:
            cut, first, last = 0, cur, cur + 1
            while first <= n:
                cut += min(n + 1,last) - first
                first *= 10
                last *= 10
                
            if cut <= k:
                cur += 1
                k -= cut
            else:
                cur *= 10
                k -= 1
        return cur
```
