## 432. All O`one Data Structure

[Problem link](https://leetcode.com/problems/all-oone-data-structure/)

- My approach

O(n), not O(1).

```python
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.dic:
            self.dic[key] += 1
        else:
            self.dic[key] = 1
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.dic:
            self.dic[key] -= 1
            if self.dic[key] == 0:
                self.dic.pop(key)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.dic:
            return ''
        m = max(self.dic.values())
        for k in self.dic:
            if self.dic[k] == m:
                return k
        return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.dic:
            return ''
        m = min(self.dic.values())
        for k in self.dic:
            if self.dic[k] == m:
                return k
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```
