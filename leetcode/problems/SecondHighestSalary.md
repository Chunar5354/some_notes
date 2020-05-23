## Approach

[Problem link](https://leetcode.com/problems/second-highest-salary/)

- My approach

To search the second highest data, we can search the maximum data from the collection which is smaller than the highest data.

```sql
select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee);
```

But if we want to search the third highest or more smaller data, it will be very complex.

There is a more universal method by using `limit`.

```sql
select ifnull((select distinct Salary from Employee order by Salary desc limit 1,1), null) as SecondHighestSalary;
```

There are three points:

  - `limit 1, 1` means we select the result from the second line to the second line
  - `ifnull((result), other)` means if the result in bracket is null, we use other to replace the result
  - `distinct` means avoid the duplicated values while selecting
