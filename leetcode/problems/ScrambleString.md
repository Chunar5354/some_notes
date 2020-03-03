## Approach

[Problem link](https://leetcode.com/problems/scramble-string/)

This problem is a little difficult so I didn't solve it.

- Other's approach

I searched for other's approach, and there is a good solution by using `DFS` (depth first search) method.

```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        '''
        作为一个递归函数，它将返回一个bool值
        每次传入的s1和s2视为上一层字符串的一个分支
        '''
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        # 如果s1和s2中的字母不相同的话，那么当前的两个分支肯定不能相等
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True  
        for i in range(1, len(s1)):
            # 要满足的条件为：s1的前i项和s2的前i项相等并且s1的后i项和s2的后i项相等
            # 或者s1的前i项和s2的后i项相等并且s1的后i项和s2的前i项相等
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(1[i:], s2[i:])) \
                or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        
        return False
```
