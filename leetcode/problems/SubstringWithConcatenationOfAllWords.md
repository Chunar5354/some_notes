## Approach

[Problem link](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

- My solution

This is a complex problem

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        l = len(words[0])
        n = len(words)
        res = []
        for i in range(len(s)-l+1):
            if s[i:i+l] in words:
                # If there are less letters than the whole length of all words, break
                if len(s) - i < n*l:
                    break
                d = {}
                # Colletct all sub words in words[]
                for j in range(i, i+n*l, l):
                    current_s = s[j:j+l]
                    # print(current_s)
                    if current_s not in words:
                        break
                    else:
                        if current_s in d:
                            d[current_s] += 1
                        else:
                            d[current_s] = 1
                # print(d)
                is_ans = True
                for word in words:
                    # If a word in words doesn't appear in dict, means it's not proper
                    # and if the count of the word in words and in dict are different, means it's not proper
                    if word not in d.keys() or d[word] != words.count(word):
                        is_ans = False
                        break
                if is_ans:
                    res.append(i)
        return res
```

This approach doesn't perform very well, but I can't find another way.

There is an approach from others:
```python
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        solu = []
        # defaultdict set a dictionary with no keys but their default value as the argument given
        # in this case, it's int
        word_map = defaultdict(int)
        if len(s) == 0 or len(words) == 0:
            return solu
        # Store the words in a dictionary
        for word in words:
            word_map[word] += 1
        
        length = len(words[0])  # length of any word
        # Because every word has the same length, so we can traverse just in the range of length
        for i in range(0, length):
            start = i
            count = 0
            curr_word_map = defaultdict(int)

            for j in range(start, len(s)-length+1, length):
                subword = s[j:j+length]

                # check if the subword exists in the map
                if subword in word_map:
                    curr_word_map[subword] += 1
                    count += 1
                    # print("found:", subword)
                    # print("current word map:", curr_word_map)
                    # print("count: ", count)

                    # if current word count of some word is larger than 
                    # that of actual num of words, reduce count and move
                    # start pointer one length further
                    
                    ## He uses the 'start' like a pointer
                    ## and count every word, if find a word's number in current word map 
                    ## is larger than in given words list(word_map): reduce count and update start
                    while(curr_word_map[subword] > word_map[subword]):
                        removed = s[start:start+length]
                        print("removing:", removed)
                        curr_word_map[removed] -= 1
                        start += length
                        count -= 1
                    # if all words have been counted in this sequence, add
                    # the answer to result
                    
                    ## If every word count passed, and total count also passed,
                    ## means this sub of s is accorded given condition, add it to result
                    if count == len(words):
                        solu.append(start)
                        # then we move one word length further and continue our
                        # search, update start
                        removed = s[start:start+length]
                        curr_word_map[removed] -= 1
                        start += length
                        count -= 1
                        #print("adding solu", start)

                else:
                    count = 0
                    start = j + length
                    curr_word_map.clear()
        return solu
```

This approach runs fast because it doesn't traverse s by every character, pay attention to `for i in range(0, length):`, 
it just traverse in the length of word, and set a pointer 'start', all the words back are according to this pointer.

## Knowledge

- defaultdict in Python

`defaultdict` is an object like dictionary, but it's value is set by default as the argument given,like:
```python
from collections import defaultdict

d = defaultdict(int)  # set the defaule value as int type
```
