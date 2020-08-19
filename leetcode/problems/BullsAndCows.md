## 299. Bulls and Cows

[Problem link](https://leetcode.com/problems/bulls-and-cows/)

- My approach

My idea is removing the same numbers with same index firstly(bulls). Then just check if every number in guess is in secret(cows), and pay attention to avoid duplication.

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = list(secret)
        g = list(guess)
        
        a = 0  # a is bull
        b = 0  # b is cow
        
        d = {}
        i = 0
        # Remove same numbers with same index, count bulls and save the remain secret in a dictionary as {number: count}
        while i < len(s):
            if s[i] == g[i]:
                a += 1
                s.pop(i)
                g.pop(i)
            else:
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
                i += 1
        
        # Count cows
        for i in g:
            if i in d:
                if d[i] > 0:
                    d[i] -= 1
                    b += 1
                    
        return '{}A{}B'.format(a, b)
```

- Other's approach

There is a more clearly method.

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = Counter(secret)

        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                # corresponding characters match
                if ch == secret[idx]:
                    # update the bulls
                    bulls += 1
                    # update the cows 
                    # if all ch characters from secret 
                    # were used up
                    cows -= int(h[ch] <= 0)
                # corresponding characters don't match
                else:
                    # update the cows
                    cows += int(h[ch] > 0)
                # ch character was used
                h[ch] -= 1
                
        return "{}A{}B".format(bulls, cows)
```
