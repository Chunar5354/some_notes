## 262. Trips and Users

[Problem link](https://leetcode.com/problems/trips-and-users/)

- Other's approach

```sql
# Write your MySQL query statement below
WITH T1 AS 
(
SELECT *
FROM TRIPS AS T
LEFT JOIN USERS AS U 
ON T.CLIENT_ID = U.USERS_ID OR T.DRIVER_ID = U.USERS_ID
WHERE  CLIENT_ID IN (SELECT DISTINCT USERS_ID FROM USERS WHERE BANNED = 'NO')
AND DRIVER_ID IN (SELECT DISTINCT USERS_ID FROM USERS WHERE BANNED = 'NO')
AND REQUEST_AT BETWEEN DATE('2013-10-01') AND DATE('2013-10-03')
)

SELECT REQUEST_AT AS DAY,
ROUND((COUNT(CASE WHEN STATUS ='cancelled_by_driver' OR STATUS = 'cancelled_by_client' THEN ID END)/COUNT(*)),2) AS 'CANCELLATION RATE'
FROM T1 
GROUP BY REQUEST_AT
```

There are some points:

- 1.Using `with... as` to create a new combination table with the given conditions.

- 2.Using `case... then` to divide groups
