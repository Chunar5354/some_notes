## 347. Top K Frequent Elements

[Problem link](https://leetcode.com/problems/top-k-frequent-elements/)

- My approach

Use two dictionaries, the first is {value: frequence}, and use the first dictionary to build the second dictionary {frequence: value}. Then find the k max frequent values.

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {value: frequence}
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        # {frequence: value}
        dd = {}
        for key in dic:
            if dic[key] in dd:
                dd[dic[key]] += [key]
            else:
                dd[dic[key]] = [key]
        
        l = list(dd.keys())
        l.sort()
        
        res = []
        while len(res) < k:
            res += dd[l[-1]]
            l.pop()
        
        return res
```

For more solutions, please see [official solution](https://leetcode.com/problems/top-k-frequent-elements/solution/)
