## Approach

[Problem link](https://leetcode.com/problems/department-top-three-salaries/)

- My approach

Because we need to select more than one row and divide groups, we can't use `limit` here.

To do group, we can select the table twice, and set a condition that `e1.Department = e2.Department`.

And to select the top three results, we can use `count`.

```sql
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;
```
