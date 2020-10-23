## 388. Longest Absolute File Path

[Problem link](https://leetcode.com/problems/longest-absolute-file-path/)

- My approach

Save the directories in a dictionary by their level. For example, if the given string is:

```
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
```

then the dictionary will be:

```
{
  1: ['dir'], 
  2: ['subdir1', 'subdir2'], 
  3: ['subsubdir1', 'subsubdir2']
}
```

When meet a string that contains '.', means it's a file, then the whole path is the sum of all the `dic[i][-1]`(i is the lower levels than current file level).

```python
class Solution:
    def lengthLongestPath(self, _input: str) -> int:
        dic = collections.defaultdict(list)
        self.res = 0
        
        def helper(idx, level):
            if idx >= len(_input):
                return
            if _input[idx] == '\n':
                curr = idx+1
                while _input[curr] == '\t':
                    curr += 1
                helper(curr, curr-idx)  # curr-idx is the length of '\n\t...', it can stand for the level of directory
            else:
                curr = idx
                isFile = False
                while curr < len(_input) and _input[curr] != '\n':
                    if _input[curr] == '.':
                        isFile = True
                    curr += 1
                if isFile:
                    length = curr - idx
                    for i in range(1, level):
                        length += len(dic[i][-1])+1  # 1 stands for '\'
                    self.res = max(self.res, length)  # if meet a file, calculate the length
                else:
                    dic[level].append(_input[idx:curr])  # if meet a directory, add it into dic
                helper(curr, level)
        
        helper(0, 1)
        return self.res
```
