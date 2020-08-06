## 274. H-Index

[Problem link](https://leetcode.com/problems/h-index/)

- My approach

My idea is sorting the list frstly, so the numbers after current number are larger than current number, `l-i` can stand for the count of citations larger then current. 

And if current number equals to l-i, means there are just l-i citations not less than current h, so l-i(or current h) is the answer.

Then is current number is larger than l-i1, means the count of citations is less then current h, so current h can't be the answer. But the definition is the count of citations 
larger than h is at least h, so h maybe not in the citations list, it can be a calculated value. And if current h is larger than l-i, means there are l-i citations which h is larger 
than l-i, so l-i is the answer.

The code is:

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = len(citations)
        for i in range(l):
            if citations[i] >= l-i:
                print(l, i)
                return l-i
        return 0
```

- Other'a approach

There is a method from others which dosn't need to sort.

```python
class Solution:
    def hIndex(self, A: List[int]) -> int:
        n = len(A)
        a = [0] * n
        for x in A:
            if x < n:
                a[x] += 1
        # Now in a, each element a[i] stands for how many h equals to i

        ct = 0
        for i in range(n):
            ct += a[i]
            # ct > n-i means there are n-i papers have no more than i conditions, so i is the answer
            if ct >= n-i:
                return i
        
        return n
```
