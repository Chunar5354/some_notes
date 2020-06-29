## Approach

[Problem link](https://leetcode.com/problems/word-search-ii/)

- My approach

Firstly I want to use DFS, but it failed. Then I tried an other's DFS approach, but it's time limit exceeded.

So I searched more other's approaches and get a method of `DFS + Trie`. By using Trie, we don't need to traverse one word many times.

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        # Create a Trie
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                curr.setdefault(c, {})
                curr = curr[c]
            curr[WORD_KEY] = word
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(board)
        n = len(board[0])
        
        # There may be one word repeated in res, so use set to avoid that
        res = set()
        def helper(r, c, curr_dic):
            if WORD_KEY in curr_dic.keys():
                res.add(curr_dic[WORD_KEY])

            # Change current character to avoid duplication
            temp = board[r][c]
            board[r][c] = '*'
            for step_r, step_c in directions:
                new_r = r + step_r
                new_c = c + step_c
                if new_r < 0 or new_c < 0 or new_r >= m or new_c >= n:
                    continue
                for k in curr_dic.keys():
                    if k == board[new_r][new_c]:
                        helper(new_r, new_c, curr_dic[k])
            # After searching, set it back
            board[r][c] = temp
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.keys():
                    helper(i, j, trie[board[i][j]])
        return list(res)
```
