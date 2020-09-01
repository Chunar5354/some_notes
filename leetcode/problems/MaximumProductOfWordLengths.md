## 318. Maximum Product of Word Lengths

[Problem link](https://leetcode.com/problems/maximum-product-of-word-lengths/)

- My approach

My idea is using and operation of collection o dheck if there are same characters in the words.

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i])*len(words[j]))
        return res
```

But every time need to translate string to collection and calculate the length of words, this method runs very slowly.

- Other'a appraoch

A smarter way to solve this problem is using `bit`.

There are only 26 characters in English, and 32-bit number can contain it. Each bit stands for one character. So we can create a unique number for each word. And 
if num1 && num2 = 0, means there are no same characters in word1 and word2.

```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0
        n = len(words)
        d = collections.defaultdict(int)
        for w in words:
            mask = 0
            for c in w:
                # Every character has its own bit, for example, 'a' is 1, 'b' is 10, and 'c' is 100, so 'ac' is 101
                mask |= 1 << ord(c) - ord('a')
            d[mask] = max(d[mask],len(w))
        large = 0

        for i in d.keys():
            for j in d.keys():
                if i&j == 0:  # i&j = 0 means there are no same characters in word1 and word2
                    large = max(large, d[i]*d[j])
        return large
```
