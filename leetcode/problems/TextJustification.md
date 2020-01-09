## Approach

[Problem link](https://leetcode.com/problems/text-justification/)

- My approach

This is a complex problem, in my idea, there are three key points:

  - 1.How to decide how many words will be in one line?
  - 2.How to deal with the whitespaces?
  - 3.How to deal with the special last line?

Then I set two functions to solve the first and second problem, and a 'if-else' judgement to deal with the third problem.
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        crt_index = 0
        def make_str(pos):
            '''
            Give current position, return a list of current words and next position
            '''
            current_length = len(words[pos])
            for i in range(pos, len(words)):
                if i >= len(words)-1:  # The final line
                    break
                current_length += 1+len(words[i+1])
                if current_length > maxWidth:
                    break
            return words[pos:i+1], i+1
        
        def divide_space(l, n):
            '''
            Give a length and how many parts to divide, return a list of divided result as average as possible
            '''
            if n == 0:  # If only one word
                return [l]
            # For example, 10 divide to 3 parts, they are [4, 3, 3]
            rem = l % n
            new_l = l + n - rem
            space_list = [int(new_l/n)] * n
            for i in range(n-rem):
                space_list[n-i-1] -= 1
            return space_list
        
        while crt_index < len(words):
            word_list, crt_index = make_str(crt_index)
            if crt_index < len(words):
                l_all = 0
                for s in word_list:
                    l_all += len(s)
                l_diff = maxWidth - l_all
                # Distribute whitespaces
                space_list = divide_space(l_diff, len(word_list)-1)
                current_s = word_list[0]
                for i in range(len(space_list)):
                    current_s += ' '*space_list[i]
                    # There may be only one word in word_list
                    try:
                        current_s += word_list[i+1]
                    except:
                        pass
            # The last line is special
            else:
                current_s = ' '.join(word_list)
                num = maxWidth - len(current_s)
                current_s += ' '*num
            res.append(current_s)
        return res
```
