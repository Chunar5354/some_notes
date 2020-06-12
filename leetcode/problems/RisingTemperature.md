## Approach

[Problem link](https://leetcode.com/problems/rising-temperature/)

- My approach

We can solve this problem by copying the table into two tables.

```sql
select w1.Id from Weather as w1, Weather as w2 
where w1.Temperature > w2.Temperature and datediff(w1.RecordDate, w2.RecordDate) = 1;
```

Pay attention to the function `datediff`, it can calculate the different of two dates, including the situation that the two days are in 
two months or two years.

We can also use `join` method to solve this problem.

```sql
select w1.Id from Weather as w1 
    join Weather as w2 on w1.Temperature > w2.Temperature 
                       and datediff(w1.RecordDate, w2.RecordDate) = 1;
```
