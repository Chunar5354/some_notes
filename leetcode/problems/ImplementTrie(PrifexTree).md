## Approach

[Problem link](https://leetcode.com/problems/implement-trie-prefix-tree/)

- My approach

My idea is very easy: just use a collection to save the words and search from it.

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.value.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.value

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # print(self.value, prefix)
        for s in self.value:
            if s.startswith(prefix):
                return True
        return False
```

But this method runs very slowly. 

- Other's approach

To create a trie, we need to set the relationship of characters. In Python we can use `dictionary` to create this relationship.

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        # Every character directs to a dictionary, and the key is characters after current character
        for char in word:
            if char not in curr:
                curr[char] = {}
                curr = curr[char]
            else:
                curr = curr[char]
        # '*' means the word is end
        curr['*'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        # Search the characters level by level
        for char in word:
            if char not in curr:
                return False
            else:
                curr = curr[char]
        # '*' in curr means currrent word is end
        if '*' in curr:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Search prefix doesn't go to end
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            else:
                curr = curr[char]
        return True
```
