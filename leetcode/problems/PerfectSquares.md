## 279. Perfect Squares

[Problem link](https://leetcode.com/problems/perfect-squares/)

- My approach

My recursing method was time limited exceeded.

- Other's approach

 Firstly, we can save the squares which are smaller than n into a list. Then do a BFS and for each current square, we just search from the squares smaller than it 
in the searching after, this can avoid the duplications.

```python
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i**2 for i in range(1, int(n**0.5)+1)][::-1]
        self.res = float('inf')

        def helper(n, curr_nums, res):
            if n == 0:
                self.res = min(res, self.res)
                return
            for i in range(len(curr_nums)):
                if curr_nums[i] <= n and res+1 < self.res:
                    helper(n-curr_nums[i], curr_nums[i:], res+1)
        
        helper(n, nums, 0)
        return self.res
```

There is a interesting thing that if we write function `helper()` like:

```python
def helper(n, curr_nums, res):
    if n < 0:
        return
    if n == 0:
        self.res = min(res, self.res)
        return
    for i in range(len(curr_nums)):
        helper(n-curr_nums[i], curr_nums[i:], res+1)   
```

It will be time limited exceeded. I think that may be caused by the function invoke.

- Dynmamic method

This problem can also be solved by dynamic method. Create a list `dp` of n+1 length and every dp[i] stands for the perfect square numbers of i.

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if( n < 3) : return n
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if(i < square):
                    break
                # dp[i-square] is the perfect square numbers of i-square, because there is a square that 'i-square+square = i', dp[i-square] + 1 can be a square number of i.
                dp[i] = min(dp[i], dp[i-square] + 1)    # +1 is for that square we are substracting.
        return dp[-1]
```


- Mathmitical method

The methods above all have O(n^2) time complex. Using mathmitical can achieve O(n).

```python
class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n:
            return 1
        
        for i in range(1, int(sqrt(n))+1): 
            if int(sqrt(n - i*i))**2 == n - i*i:
                return 2
        
        while n % 4 == 0:
            n //= 4
            
        if n % 8 == 7:
            return 4
        else:
            return 3
```

But how to find this regular?
