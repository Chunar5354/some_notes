## 357. Count Numbers with Unique Digits

[Problem link](https://leetcode.com/problems/count-numbers-with-unique-digits/)

- My approach

The unique numbers of larger digit can be calculated by the unique numbers of smaller digits.

```python
dp = [1] * 9
dp[1] = 9
for i in range(2, 9):
    dp[i] = dp[i-1] * (11-i)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return sum(dp[:n+1])
```

Or

```python
dp = [1] * 9
for i in range(1, 9):
    dp[i] = dp[i-1]*(10-i) + sum(dp[:i])

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return dp[n]
```
