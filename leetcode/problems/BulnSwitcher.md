## 319. Bulb Switcher

[Problem link](https://leetcode.com/problems/bulb-switcher/)

- My approach

After n round switching, only the bulbs at `i^2` position will stay on.

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)
```
