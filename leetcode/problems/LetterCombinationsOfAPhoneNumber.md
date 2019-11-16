## 解题

[题目链接](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

自己做出来了，成绩不错，但是略复杂，看注释吧：
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '0' in digits or '1' in digits or len(digits) < 1:
            return []
        # 数字与字符串的对应
        s_dict = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz',
                 }
        # len_all是最终结果列表的长度，计算方法是每个数字对应的字符串的长度之积
        # last_len是上一个数字对应的字符串长度，因为在结果中，后面的字符串有多长就意味着前面的字符要重复几次
        # 例如给出的数字字符串为'23'，'3'对应的'def'长度为3，那么结果中'2'对应的字符串中每个字符要重复3次：['ad', 'ae', 'af', 'bd' ...]
        len_all = last_len = 1
        for i in range(len(digits)):
            len_all *= len(s_dict[digits[i]])
        for i in range(len(digits)):
            # 从后往前查询
            n = len(digits) - i - 1
            # 如果是最后一个数字，则初始化一个结果列表，最后面的数字对应的字符按顺序要重复（总长度 / 该数字对应字符个数）次
            if i == 0:
                res = list((s_dict[digits[n]] * int(len_all/len(s_dict[digits[n]]))))
            else:
                last_len *= len(s_dict[digits[n+1]])

                # 之后的数字对应的字符，首先要每个字符连续重复（该数字后面所有数字各自对应的字符个数之积）次
                # 然后再整体重复（总长度 / 该数字以及后面所有数字各自对应的字符个数之积）次
                # 例如，给出的数字为'567'，则'6'对应的每个字符要首先连续重复（'7'对应的长度）次：mmmmnnnnoooo
                # 然后再整体重复总长度（3*3*4）/('7'对应的长度（4）* 当前数字'6'对应字符数（3）)次，就是'mmmnnnnoooom'*3
                cur_list = ''.join([k*last_len for k in s_dict[digits[n]]] * int(len_all/(last_len*len(s_dict[digits[n]]))))
                # 最终结果就是每一次的列表对应位置相加
                res = [cur_list[j] + res[j] for j in range(len(res))]
        return res
```

这样实现速度也挺快，但是不是很容易理解，官方给出的答案使用了递归，似乎是一种更好的选择
```python
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                # 加完了就把结果添加到output中
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                # 对当前数字对应的每一个字符进行遍历
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    # combination是前面所有字符的拼接，再加上当前字符，然后对之后的数字做相同操作
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
```

递归的方法实现起来代码非常简单，只是设计的时候判断条件什么的不太好想

### 结论

- 对于重复性操作的题目，想想递归，往往逻辑上比较简单，也比较高级
