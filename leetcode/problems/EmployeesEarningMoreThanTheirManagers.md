## Approach

[Problem link](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

- My approach

To solve this problem, we need to search the table twice. So we can use `join` to connect the two searching.

```sql
# Write your MySQL query statement below
SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
;
```
