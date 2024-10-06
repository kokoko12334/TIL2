# Write your MySQL query statement below
SELECT s.user_id, ROUND(IFNULL( COUNT(case when c.action ='confirmed' then 1 end)/NULLIF(COUNT(c.action),0),0),2) as confirmation_rate
FROM signups as s
LEFT JOIN confirmations as c ON s.user_id = c.user_id
GROUP BY s.user_id



// NULLIF(COUNT(c.action), 0) => 만약 해당 값이 0이면 null
// IFNULL(COUNT(c.action), 0) => 만약 해당 값이 null이면 0