## 273. Integer to English Words

[Problem link](https://leetcode.com/problems/integer-to-english-words/)

- My approach

The key point is dividing the number three digits as a group.

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        # Firstly store the special words into three dictionaries
        nums = {'0' : '',
                '1' : 'One ',
                '2' : 'Two ',
                '3' : 'Three ',
                '4' : 'Four ',
                '5' : 'Five ',
                '6' : 'Six ',
                '7' : 'Seven ',
                '8' : 'Eight ',
                '9' : 'Nine ',
                '10' : 'Ten ',
                '11' : 'Eleven ',
                '12' : 'Twelve ',
                '13' : 'Thirteen ',
                '14' : 'Fourteen ',
                '15' : 'Fifteen ',
                '16' : 'Sixteen ',
                '17' : 'Seventeen ',
                '18' : 'Eighteen ',
                '19' : 'Nineteen ',
                }
        
        tens = {'0' : '',
                '1' : 'Ten ',
                '2' : 'Twenty ',
                '3' : 'Thirty ',
                '4' : 'Forty ',
                '5' : 'Fifty ',
                '6' : 'Sixty ',
                '7' : 'Seventy ',
                '8' : 'Eighty ',
                '9' : 'Ninety ',}
        
        digits = {0 : '',
                  1 : 'Thousand ',
                  2 : 'Million ',
                  3 : 'Billion '}
        
        res = ''
        s = str(num)
        count = 0  # count stands for the groups of three digits
        
        while len(s) > 0:
            curr = s[-3:]
            # To avoid the situations such as 1000000
            if int(curr) > 0:
                res = digits[count] + res
            
            if curr[-1] == '0':
                # The last digit is 0 means it's a tens number or zero
                if len(curr) > 1:
                    res = tens[curr[-2]] + res
                else:
                    res = 'Zero ' + res
            # Deal with 10~19
            elif curr[-2:] in nums:
                res = nums[curr[-2:]] + res
            else:
                res = tens[curr[-2]] + nums[curr[-1]] + res
            # Hundreds
            if len(curr) == 3 and curr[0] != '0':
                res = nums[curr[0]] + 'Hundred ' + res
            count += 1
            s = s[:-3]
            
        return res[:-1]            
```
