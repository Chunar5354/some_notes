## 423. Reconstruct Original Digits from English

[Problem link](https://leetcode.com/problems/reconstruct-original-digits-from-english/)

- My approach

In English words from 0-9, there are some special characters: 'z' only in 0(zero), 'w' only in 2(two), 'u' only in 4(four), 'x' only in 6(six) and 'g' only in 8(eight).

Then for the remained 5 numbers, 'o' only in 1(one), 'r' only in 3(three), 'f' only in 5(five), 's' only in 7(seven), 'i' only in 9(nine).

So when meet these special characters, we can determine there must be the corresponding number.

```python
class Solution:
    def originalDigits(self, s: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        nums = {0: 'zero', 1: 'one', 2: 'two', 3:'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        special = {0: 'z', 2: 'w', 4: 'u', 6: 'x', 8: 'g'}
        notSpecial = {1: 'o', 3: 'r', 5: 'f', 7: 's', 9: 'i'}
        

        res = [0] * 10
        for n in special:
            # check if the special character is in dic
            while special[n] in dic and dic[special[n]] >= 1:
                res[n] += 1
                for i in nums[n]:  # reduce all the characters of this number
                    dic[i] -= 1
        
        for n in notSpecial:
            while notSpecial[n] in dic and dic[notSpecial[n]] >= 1:
                res[n] += 1
                for i in nums[n]:
                    dic[i] -= 1
        
        return ''.join(str(i)*res[i] for i in range(10))
```
