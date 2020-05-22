## Approach

[Problem link](https://leetcode.com/problems/combine-two-tables/)

- My approach

This is the first time I meet a problem of `sql`.

To conmbine two tables, MySQL provides a method `join`, and in this problem, we should use `left join`.

For more details about `join`, please see [here](https://blog.csdn.net/Jintao_Ma/article/details/51260458)

```sql
SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
on Person.PersonId = Address.PersonId;
```

And if we use a parameter to represent the table name, it will run faster.

```sql
select p.FirstName, p.LastName, a.City, a.State from Person p left join Address a on p.PersonId = a.PersonId;
```
