## Approach

[Problem link](https://leetcode.com/problems/delete-duplicate-emails/)

- My approach

We can solve this problem by making the table to two same tables.

```sql
delete p1 from Person as p1, Person as p2 where p1.Email = p2.Email and p1.Id > p2.Id;
```

And there is a method to create a derived table.

```sql
DELETE
FROM Person 
WHERE Id
NOT IN (select id from (SELECT MIN(ID) as Id
       FROM Person
       GROUP BY Email) t1)
```

Pay attention to the `t1`, when create a dreived table, we must give it a alia.
