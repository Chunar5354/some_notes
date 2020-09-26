## 352. Data Stream as Disjoint Intervals

[Problem link](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

- My approach

My idea is using a dictionary to save the numbers as: {value: interval}. When a new number `val` comes, check if val in dic or val-1 and val+1 in dic.

If both val-1 and val+1 in dic, all the number between dic[val-1][0] and dic[val+1][1] needs to modify to (dic[val-1][0], dic[val+1][1]), because current val connects them.

And if val-1 in dic, all the numbers from dic[val-1][0] to val needs to modify to (dic[val-1][0], val). Then for val+1, the values needs to modify to (val, dic[vlal+1][1]).

```python
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def addNum(self, val: int) -> None:
        if val in self.dic:
            return
        if val-1 in self.dic and val+1 in self.dic:
            curr = (self.dic[val-1][0], self.dic[val+1][1])        
        elif val-1 in self.dic:
            curr = (self.dic[val-1][0], val)
        elif val+1 in self.dic:
            curr = (val, self.dic[val+1][1])
        else:
            curr = (val, val)
        
        for n in range(curr[0], curr[1]+1):
                self.dic[n] = curr

    def getIntervals(self) -> List[List[int]]:
        # Get all unique intervals and sort them
        l = list(set(self.dic.values()))
        l.sort()
        return l


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
```

- Other's approach

If we create the disjoint intervals while adding numbers, the code will run faster.

```python
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val in self.seen:
            return
        self.seen.add(val)
        if not self.l:
            self.l = [[val,val]]
            return
        # Use binary search tree to find the position of current val
        ind = bisect.bisect_left(self.l,[val,val])

        if ind>0 and ind-1<len(self.l) and self.l[ind-1][1]==val-1:
            if ind<len(self.l) and self.l[ind][0]==val+1:
                start, end = self.l[ind-1][0],self.l[ind][1]
                self.l[ind-1:ind+1] = [[start,end]]
            else:
                self.l[ind-1][1]=val
        else: #cannot merge with former
            if ind<len(self.l) and self.l[ind][0]==val+1:
                #check if we can merge 
                self.l[ind][0] = val
            else:
                self.l.insert(ind,[val,val])

    def getIntervals(self) -> List[List[int]]:
        return self.l
```
