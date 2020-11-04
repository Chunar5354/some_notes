## 399. Evaluate Division

[Problem libk](https://leetcode.com/problems/evaluate-division/)

- Other's approach

We can see the structure as a directed graph, and the nodes are the characters in equations, the lines are the quotient fron head to tail.

Then we can do DFS for this graph, if the two nodes are not connected, return -1.
