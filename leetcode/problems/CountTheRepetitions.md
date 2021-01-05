## 466. Count The Repetitions

[Problem link](https://leetcode.com/problems/count-the-repetitions/)

- Other's approach

The key point is to find `cycle`. When find a repeated pattern that contains s1, check how many s1 is in this pattern. So we can find how many s2 can be contained in the whole 
s1*n1.

```python
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # hashtable to store the patterns
        patterns = {}

        # pointers on s1 and s2
        p1, p2 = 0, 0

        # number of occurance of s1 and s2 so far
        c1, c2 = 1, 0

        # execute the loop when number of occurance of s1 has not been used up
        while c1 <= n1:
            print(c1, c2)

            # if a character match is found, move p2 forward
            if s1[p1] == s2[p2]:
                p2 += 1

                # p2 reaches the end of s2, meaning 1 occurance of s2
            if p2 == len(s2):
                c2 += 1
                p2 = 0

                # store the pattern if not exists
                if p1 not in patterns:
                    patterns[p1] = (c1, c2)

                # a repeat has been found, handle the repeat
                else:
                    # previous occurance of s1 and s2
                    prev_c1, prev_c2 = patterns[p1]

                    # number of occurance of s1 and s2 in a single repeat
                    n_s1_repeat, n_s2_repeat = c1 - prev_c1, c2 - prev_c2

                    # number of repeats
                    n_repeats = (n1 - prev_c1) // n_s1_repeat
                    print(n_s1_repeat, n_s2_repeat, n_repeats)

                    # number of s2 occurances in the repeats
                    c2_repeats = n_repeats * n_s2_repeat

                    # the remain available occurances of s1
                    remain_c1 = (n1 - prev_c1) % n_s1_repeat

                    # update c1 and c2
                    c1 = n1 - remain_c1
                    c2 = c2_repeats + prev_c2

            # move forward p1 every iteration
            p1 += 1

            # p1 reaches the end of s1, move it back to 0 and mark 1 occurance of s1
            if p1 == len(s1):
                c1 += 1
                p1 = 0
    
        print(patterns)
        # divide c2 by n2 to get the result
        return c2 // n2
```
