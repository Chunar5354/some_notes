## Approach

[Problem link](https://leetcode.com/problems/nth-highest-salary/)

- My approach

This problem creates a function in sql.

There is a point that in sql query, there can't be expression such as `N-1`. So if we want to calculate some values, we should declare 
a parament before.

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
# Create a new parament M = N-1
DECLARE M INT;
SET M=N-1;
RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT M, 1
  );
END
```
