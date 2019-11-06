## 解题

[题目链接](https://leetcode.com/problems/reverse-integer/solution/)

今天绝对大成就：

>Runtime: 28 ms, faster than 99.36% of Python3 online submissions for Reverse Integer.   
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

不过这题不算难，一下就想到了把数字转换成字符串再用列表排序，其实关键于列表倒序的算法`l.reverse()`，它是内置的：
```python
class Solution:
    def reverse(self, x: int) -> int:
    '''
    Convert int x into string x, split string into list, then reverse it
    '''
        if x > 2 ** 31 - 1 or x < - 2 ** 31 or x == 0:
            return 0
        if x > 0:
            l = [i for i in str(x)]
            l.reverse()
            res = int(''.join(l))
            if res > 2 ** 31 - 1:
                return 0
            else:
                return res
        else:
            l = [i for i in str(x)][1:]
            l.reverse()
            res = -int(''.join(l))
            if res < - 2 ** 31:
                return 0
            else:
                return res
```

看了官方的解答和其他人的一些答案，还有一种比较常见的方法是对这个整数逐位除以10取余：`n = x % 10`，然后从最低位开始反向相加：`res = res * 10 + n`

官方的java答案：
```python
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            // 判断是否溢出（这里的pop表示个位数字是否大于7或者小于-8，因为区间是[-2147483648, 2147483647]）
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

### 结论

- 对于整数的操作，一个思路是`逐位取余`

## 知识点

- Python中的`list.reverse()`，源码没查到，但内部实现的方式可能是交换下标（因为和l.reverse()的方法提交之后运行的时间相同）：
```
l = []
n = len(l)
for i in range(n // 2):
    l[i], l[n-1-i] = l[n-1-i], l[i]
```
