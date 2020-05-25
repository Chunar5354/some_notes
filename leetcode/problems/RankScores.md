## Approach

[Problem link](https://leetcode.com/problems/rank-scores/)

To solve the rank problem, we can use MySQL function `DENSE_RANK`. This function can rank the values order by certain data.

```sql
select Score, dense_rank() over (order by Score desc) as 'Rank' from Scores;
```

Pay attention to the usage `dense_rank() over()`. And the new name after `as` should be in quotes.

For more details of `DENSE_RANK` please see [here](https://www.begtut.com/mysql/mysql-dense_rank-function.html).
