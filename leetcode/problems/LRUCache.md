## Approach

[Problem link](https://leetcode.com/problems/lru-cache/)

- My approach

The key point is to record the order of using keys.

Here I use a list and each time modify current key to the last position.

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        # To record the last recently used element
        self.lru = []

    def get(self, key: int) -> int:
        if key not in self.dic.keys():
            return -1
        else:
            # Modify current key to the last position
            self.lru = [i for i in self.lru if i != key] + [key]
            return self.dic[key]

    def put(self, key: int, value: int) -> None:
        self.lru = [i for i in self.lru if i != key] + [key]
        self.dic[key] = value
        # If overflowed, delete the first element of lru in dic
        if len(self.dic.keys()) > self.capacity:
            to_delete = self.lru.pop(0)
            del self.dic[to_delete]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

And this method can be improved by a module `OrderedDict`.

- Other's approach

`OrderedDict` is a dicionary which can record the order of keys visited in the dictionary.

Here is the [official document](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict)

```python
import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
```
