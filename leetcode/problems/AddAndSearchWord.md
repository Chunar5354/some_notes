## Approach

[Problem link](https://leetcode.com/problems/add-and-search-word-data-structure-design/)

- My approach

My idea is using Trie like [Implement Trie (Prifex Tree)](https://github.com/Chunar5354/some_notes/blob/master/leetcode/problems/ImplementTrie(PrifexTree).md).

```python
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.words
        for c in word:
            if c not in curr.keys():
                curr[c] = {}
            curr = curr[c]
        # The falg of end
        curr['*'] = {}


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        jud = []
        def helper(dic_list, idx):
            if not dic_list:
                return
            if idx >= len(word):
                # We need to check if the word is search over or it's just a prefix
                for dic in dic_list:
                    if '*' == dic or '*' in dic.keys():
                        jud.append(1)
                return
            for dic in dic_list:
                # '.' can represent and character
                if word[idx] == '.':
                    new_list = [dic[k] for k in dic.keys()]
                else:
                    new_list = [dic[k] for k in dic.keys() if k == word[idx]]
                helper(new_list, idx+1)
                
        helper([self.words], 0)
        # After searching, if jud is not empty means there is at last one available word
        if jud:
            return True
        else:
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

- Other's approach

There is a more clear method to save words in a dictionary by using the length of words as key.

```python
class WordDictionary:

    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        # All the words with the same length will be saved in one list
        if word:
            self.word_dict[len(word)].append(word)
            
    def search(self, word):
        if not word:
            return False
           
        if '.' not in word:
            return word in self.word_dict[len(word)]
        
        for w in self.word_dict[len(word)]:
            success = True
            for index, ch in enumerate(word):
                if ch != w[index] and ch != '.':
                    success = False
                    break
            
            if success:
                return True
        return False
```
