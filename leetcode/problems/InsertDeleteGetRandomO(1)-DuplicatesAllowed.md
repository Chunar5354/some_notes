## 381. Insert Delete GetRandom O(1) - Duplicates allowed

[Problem link](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)

- My approach

An extension of [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/).

There are dpulicates, so we need to store the indexes of the same number. Here we use collection.

```python
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(set)
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        ret = True
        if val in self.d:
            ret = False
        self.l.append(val)
        self.d[val].add(len(self.l)-1)
        return ret
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.d[val]:
            return False
        else:
            idx = self.d[val].pop()  # get one index randomly
            last = self.l[-1]
            self.l[idx] = last  # modify it in list

            self.d[last].add(idx)  # modify it in dictionary
            self.d[last].discard(len(self.l)-1)
            self.l.pop()
            return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

