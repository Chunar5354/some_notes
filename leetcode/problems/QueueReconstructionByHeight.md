## 406. Queue Reconstruction by Height

[Problem link](https://leetcode.com/problems/queue-reconstruction-by-height/)

- My approach

Divide the people by the number of larger front people(p[1]), and sort every group by decsending order.

For example:

```
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

{0: [[7, 0], [5, 0]],
 1: [[7, 1], [6, 1]], 
 2: [[5, 2]],
 4: [[4, 4]],} 
```

Then for the '0' group, just add it to the result in ascending order. And for other groups, traverse current result, and if find n people taller than current person which 
n equals to current p[1], insert current person at index+1.

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        dic = {}
        for p in people:
            if p[1] in dic:
                dic[p[1]].append(p)
            else:
                dic[p[1]] = [p]
        for k in dic:  # divide groups by the number of taller front people
            dic[k].sort()
            dic[k].reverse()
        print(dic)
        res = []
        for k in sorted(list(dic.keys())):
            for p in dic[k]:
                if not res:
                    res.append(p)
                    continue
                n = 0
                for i in range(len(res)):
                    if res[i][0] >= p[0]:
                        n += 1
                    if n >= p[1]:
                        if k == 0:
                            res.insert(i, p)
                        else:
                            res.insert(i+1, p)
                        break
                    
        return res
```

- Other's approach

There is a more simple solution.

Firstly sort the people by the descendong order of p[0], and ascending order of p[1].

For example:

```
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
```

Now for every person, all the people before are taller than current p, so we can use its second element as index to insert it in result.

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        queue = []
        for q in people:
            queue.insert(q[1], q)
        return queue
```
