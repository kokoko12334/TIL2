# Write your MySQL query statement below
SELECT contest_id, round(count(contest_id)*100/(select count(user_id) from users),2) as percentage
FROM register r
LEFT JOIN users u ON r.user_id = u.user_id
GROUP BY contest_id
order by percentage desc, contest_id