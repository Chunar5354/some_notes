## Approach

[Problem link](https://leetcode.com/problems/department-highest-salary/)

- My approach

We can use `join...on` to connect two tables.

```sql
# Write your MySQL query statement below
select d.Name as 'Department', e.Name as 'Employee', e.Salary
from Employee as e join Department as d on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) in (select departmentId, max(Salary) from Employee group by DepartmentId);
```
