## Approach

[Problem link](https://leetcode.com/problems/gas-station/)

- My approach

Firstly I used a brute force method.

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If want to finished the circle, all the gas in 'gas' must be more than or equal to 'cost'
        if sum(gas) - sum(cost) < 0:
            return -1
        canStart = []
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
            if gas[i] >= cost[i]:
                canStart.append(i)
        def helper(idx):
            crt_diff = diff[idx:] + diff[:idx]
            # crt_diff[i] stands for the gas from start to current station, if crt_diff[i] < 0, means can't go to next station
            for i in range(1, len(crt_diff)):
                crt_diff[i] += crt_diff[i-1]
                if crt_diff[i] < 0:
                    return False
            return True
        for start in canStart:
            res = helper(start)
            if res:
                return start
        return -1
```

But this method need to do traverse for every possible start,it runs slowly.

Inspired by others, there is a modified method.

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If want to finished the circle, all the gas in 'gas' must be more than or equal to 'cost'
        if sum(gas) - sum(cost) < 0:
            return -1
        s = 0
        cur_tank = 0
        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]
            # cur_tank is the gas until current station, if cur_tank < 0, means the stations before current station can't be the start
            # So we modify the start station to the next station
            if cur_tank < 0:
                cur_tank = 0
                s = i + 1
        return s
```
