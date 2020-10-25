## 390. Elimination Game

[Problem link](https://leetcode.com/problems/elimination-game/)

- My approach

I used step-by-step method, but it was time limited exceeded.

- Other's approach

Every time the interval of numbers are increasing by 2, if we can find the start number, then we can confirm all the numbers.

See the [explanation](https://leetcode.com/problems/elimination-game/discuss/699816/Python-simple-solution-with-examples)

```python
class Solution:
    def lastRemaining(self, n: int) -> int:
        i = 0
        start = 1
        diff = 1
        while( n > 1 ):
            i += 1
            if( i == 1):
                start = 2
            n = n // 2
            if(n == 1):
                return start
            diff = diff * 2
            #1 #3
            # when, we have odd number of elements and level is reverse level i.e i % 2 ==1, then starting ele will be deleted, so our start will be start + diff (check above examples)
            #2
            if( (i % 2 == 1 and n % 2 == 1) or (i % 2 == 0) ): start = start + diff
        return start
```
