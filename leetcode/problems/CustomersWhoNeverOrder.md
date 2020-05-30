## Approach

[Problem link](https://leetcode.com/problems/customers-who-never-order/)

- My approach

Check if data from table 1 is in the select result of table 2.

```sql
# Write your MySQL query statement below
select c.name as Customers from Customers as c where c.Id not in (select CustomerId from Orders);
```
