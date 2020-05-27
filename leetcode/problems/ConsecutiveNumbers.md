## Approach

[Problem link](https://leetcode.com/problems/consecutive-numbers/)

- My approach

To solve this problem, we can use `and` method to select three consecutive numbers.

```sql
# Write your MySQL query statement below
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;
```

And there is another method.

```sql
select distinct Num as ConsecutiveNums from Logs
where (Id+1,Num) in (select Id, Num from Logs) 
and (Id+2,Num) in (select Id, Num from Logs)
```
