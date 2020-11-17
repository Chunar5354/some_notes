## 414. Third Maximum Number

[Problem link](https://leetcode.com/problems/third-maximum-number/)

- My approach

Use a window of 3 length, when meet a nuber larger than the minimum number in window, pop the minimum number and add current number in window.

```python
class Solution:
    
    def thirdMax(self, nums) -> int:
        window = set()
        for n in nums:
            if n in window:
                continue
            if len(window) < 3:
                window.add(n)
            else:
                if n > min(window):
                    window.remove(min(window))
                    window.add(n)
        if len(window) < 3:
            return max(window)
        return min(window)
```
