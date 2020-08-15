## 290. Word Pattern

[Problem link](https://leetcode.com/problems/word-pattern/)

- My approach

Firstly split the ste with whitespace. Then create two dictionaries to save the map from pattern to str and from str to pattern. If there is a map different with the existing map, 
return False.

```python
class Solution:
    def wordPattern(self, pattern: str, _str: str) -> bool:
        l = _str.split(' ')
        if len(l) != len(pattern):
            return False
        
        dp = {}
        dl = {}
        for i in range(len(l)):
            if pattern[i] not in dp:
                dp[pattern[i]] = l[i]
            else:
                if l[i] != dp[pattern[i]]:
                    return False
            
            if l[i] not in dl:
                dl[l[i]] = pattern[i]
            else:
                if pattern[i] != dl[l[i]]:
                    return False
        return True
```

- Official solution

We can solve this problem by using only one dictionary. Save the pattern and words from str in a same dictionary as key, and their values are the indexes. If the key is already in 
dictionary we do not change it, else dic[key] = index. And if current pattern and word have different values, return False.

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_index = {}
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True
```

