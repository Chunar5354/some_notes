## 336. Palindrome Pairs

[Problem link](https://leetcode.com/problems/palindrome-pairs/)

- My approach

My method is brout force with a little filter.

```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalind(s):
            return s == s[::-1]
        
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not words[i]:
                    if isPalind(words[j]):
                        res += [[i, j], [j, i]]
                    continue
                if not words[j]:
                    if isPalind(words[i]):
                        res += [[i, j], [j, i]]
                    continue
                # If two words can compose a paindrome, the first character of left word must euqals to the last character of the right word
                if words[i][0] == words[j][-1]:
                    if isPalind(words[i] + words[j]):
                        res.append([i, j])
                if words[i][-1] == words[j][0]:
                    if isPalind(words[j] + words[i]):
                        res.append([j, i])
        return res
```

This mehod will check many words[i] + words[j], it can takes nearly O(n^3) time complexity.


- Other's approach

To save the time, we can save the words in a dictionary. And the key point of the method below is dividing the words into two parts: `prefix and suffix`.

For a word w, if the prefix of w(w[:j]) in the dictionary and the suffix of w(w[:j]) is a palindrome itself, so `prefix + suffix + prefix` is a palindrome. So as the suffix.

```python
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {w[::-1]: i for i, w in enumerate(words)}
        res = []
        
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre = w[:j]
                suf = w[j:]
                if pre in dic and dic[pre] != i and suf[::-1] == suf:
                    res.append([i, dic[pre]])
                # If both words[i]+words[j] and words[j]+words[i] are palindrome, there will be duplication in res, to avoid this situation, we start suffix from 1.
                if j > 0 and suf in dic and dic[suf] != i and pre[::-1] == pre:
                    print(suf)
                    res.append([dic[suf], i])
        
        return res
```
