## 解题

[题目链接](https://leetcode.com/problems/regular-expression-matching/)

这个题好难，要判断的条件太多了，整理一下：

依次对两个字符串进行遍历，在不超过原字符串长度的条件下，判断p中当前字符(p[j])的下一位是否为`*`
- 1 若为`*`，则有两种情况：
  - 1.1 `*`前面的字符在s中要重复出现，比如这种情况：
  ```
  s = 'aaaab'
  p = 'a*b'
  ```
  要判断`*`前面的字符和s中对应位置(s[i])的字符是否相等，如果相等（包括`*`前面的字符为`.`的情况），就对s[i+1:]和p[j:]再次进行判断（递归）
 
  - 1.2 `*`前面的字符在s中对应的位置没有，比如：
  ```
  s = 'aaaab'
  p = 'c*b'
  ```
  因为`*`符号表示它前面的字符又x个，而x可以为0，所以在这种情况下，要对s[i:]和p[j+2:]再次进行判断（递归）

- 2 若不为`*`，则要看s[i]与p[j]是否相等（包括`.`字符），如果相等，则从s[i+1:]和p[j+1:]继续判断（递归）；如果不相等，则函数结束，返回False

自己做的时候被绕蒙了，看了官方的答案，最优解是这个：
```python
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        # 嵌套了一个递归函数
        def dp(i, j):
            if (i, j) not in memo:
                # 如果字符串p已经遍历完，而s还没有，说明二者不匹配
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    # 判断p中的字符和s中对应位置的字符是否相等，或为'.'
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    # 如果p的下一个字符是'*'
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        # dp(i, j+2)对应前面说的情况中的1.2
                        # dp(i+1, j)对应情况1.1
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        # dp(i+1, j+1)对应情况2
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans   # 为什么不把结果存在memo里面就要慢很多？
            return memo[i, j]

        return dp(0, 0)  # 从s[0], p[0]开始判断
```

这里有一个很有意思的现象，当把`memo[i, j] = ans`这一句注释掉，直接`return ans`的时候，运行的时间会极具增加（1756ms，而原本只有28ms）
