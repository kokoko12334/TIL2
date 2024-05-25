# Write your MySQL query statement below

SELECT name
FROM
(SELECT e.name, count(e.id) as cnt
FROM employee e
LEFT JOIN employee e2 ON e.id = e2.managerId
GROUP BY e.id) AS sub
WHERE cnt >= 5




SELECT e.name
FROM employee e
LEFT JOIN employee e2 ON e.id = e2.managerId
GROUP BY e.id
HAVING count(e.id) >= 5