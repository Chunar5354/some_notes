## Approach

[Problem link](https://leetcode.com/problems/climbing-stairs/)

- My approach

Firstly I tried recursing method, but time exceeded.

And then I used a mathmatical method.

The idea is calculating every answer from no '2' to the most '2', for example, if the given n is `5`:
```
There can be at most two '2' in the answers, so:

no '2': '11111'
one '2': '2111', '1211', '1121', '1112'
two '2': '221', '212', '122'

The result is 1 + 4 + 3 = 8 
```

Here is the code:
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Calculate how many '2' can most be in the answers
        num_of_two = n // 2
        res = 0
        for i in range(1, num_of_two+1):
            # 'positions' means how many positions '2' can be inserted in '1's
            positions = n - 2*i +1
            den = 1
            num = 1
            # Current answer equals to (positions*(posisioins+1)*...*(positions+i-1) / i*(i-1)*...*1)
            # And this is the answer of i '2's in the steps
            for j in range(i):
                den *= (positions+j)
                num *= (i-j)
            res += int(den/num)
        # Finally the result equals to the sum of (one '2', two '2' ... until num_of_two '2') plus no '2', which has only on asnwer
        return res+1
```

- Official approach

There are many official approachs, including recursing, dynamic and fibonacci methods.

The recursing and finonacci methods are a little complex, 
you can see more details from [official solution](https://leetcode.com/problems/climbing-stairs/solution/).

But I think the dynamic method is smart and easy.
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        steps = [0] * n
        steps[0] = 1
        steps[1] = 2
        # Thw ways of current point equals to the sum of i-1 and i-2 point
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n-1]
```

