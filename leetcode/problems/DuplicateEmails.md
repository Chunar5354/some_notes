## Approach

[Problem link](https://leetcode.com/problems/duplicate-emails/)

- My approach

We can use `join` to select the table twice.

```sql
# Write your MySQL query statement below
select distinct a.Email from Person as a join Person as b where a.Email = b.Email and a.Id != b.Id;
```
