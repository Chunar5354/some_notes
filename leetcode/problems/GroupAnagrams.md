## Approach

[Problem link](https://leetcode.com/problems/group-anagrams/)h

- My approach

Unexpectedlly my diea is the same as official approach.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Set a dictionary which key: value is as 
        # sorted_str: list_str
        d = {}
        res = []
        
        for s in strs:
            # Transform str into list, then sort it, and transform the sorted list into a new str, as the key
            # (beceuse list can't be the key od a dictionary), and the value of 'd' is str list.
            list_s = list(s)
            list_s.sort()
            sorted_s = ''.join(list_s)
            if sorted_s not in d.keys():
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        for k in d.keys():
            res.append(d[k])
        return res
```

And the offical approach uses `tuple` as the key oof dictionary.
```python
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        # Set the default type of the value to list
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```

And there is also a method by using `unicode`.
```python
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            # Set a 26 length list which default value is 0
            count = [0] * 26
            for c in s:
                # For each character, add 1 to the corresponding position
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```
