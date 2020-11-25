## 424. Longest Repeating Character Replacement

[Problem link](https://leetcode.com/problems/longest-repeating-character-replacement/)

- Other's approach

Use slide window, and count the most frequent character in window, then check if the `length of window` > `k + the largest frequence`, if the window is large, slide it to right.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = collections.defaultdict(int)
        most_num = 0
        
        res = 0
        for end in range(len(s)):
            freq[s[end]] += 1
            most_num = max(most_num, freq[s[end]]) # get the largest frequence in window
            while end-start+1 > most_num+k:
                freq[s[start]] -= 1  # modify the frequence
                start += 1  # slide thw window
            res = max(res, end-start+1)
        return res
```
