## 380. Insert Delete GetRandom O(1)

[Problem link](https://leetcode.com/problems/insert-delete-getrandom-o1/)

- My approach

Use one dictionary and one list to store the elements. When an element is inserted, just add it at the end of list, then store it as {value: index-of-list} in dictionary.
And when delete an element, firstly get its index from dictionary, then modify the position of list[idx] to list[-1], nextly pop the last element in list and modify dictionary, then 
delete the given val.

```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        else:
            self.l.append(val)
            self.d[val] = len(self.l)-1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        else:
            idx = self.d[val]
            self.l[idx] = self.l[-1]
            self.d[self.l.pop()] = idx
            self.d.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.choice(self.l)
    
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
