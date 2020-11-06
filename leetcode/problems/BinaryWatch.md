## 401. Binary Watch

[Problem link](https://leetcode.com/problems/binary-watch/)

- My approach

In my solution, the key idea is to find the m combination from a n-length array, here I use recursing.

```python
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        h = [1, 2, 4, 8]
        m = [1, 2, 4, 8, 16, 32]
        
        def helper(n, l):  # get n combination from l
            if n == 0:
                return [0]
            if n == 1:
                return l
            ans = []
            for i in range(len(l)):
                ans += [l[i]+j for j in helper(n-1, l[i+1:])]
            return ans
        
                        
        res = []
        for i in range(num+1):
            # i stands for there are i LEDs of hour are on, so there can be num-i LEDs of minute are on
            # h
            hours = helper(i, h)
            # m
            minutes = helper(num-i, m)
            # get all the possible combinations of hours and minutes, then compose them
            for hh in hours:
                if hh > 11:
                    continue
                for mm in minutes:
                    if mm > 59:
                        continue
                    if mm < 10:
                        res.append(str(hh) + ':0' + str(mm))
                    else:
                        res.append(str(hh) + ':' + str(mm))
        return res      
```


- Other's approach

For this problem, each LED stands for a number of `2^n`, so we can check for the bits of the numbers, a bit '1' can represent a lighting LED.

```python
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for i in range(0, 12):
            for j in range(0, 60):
                if  (bin(i)+bin(j)).count('1') == num:
                    res.append('%d:%02d'%(i,j))  # %02d to format the length
        return res
```
