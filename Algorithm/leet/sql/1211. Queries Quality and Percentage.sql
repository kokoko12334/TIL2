# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating/position),2) as quality, ROUND(COUNT(CASE WHEN rating < 3 THEN 1 END)*100/COUNT(rating),2) as poor_query_percentage
FROM queries
GROUP BY query_name
HAVING query_name is not null




# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating/position),2) as quality, ROUND(sum(rating < 3) *100/COUNT(rating),2) as poor_query_percentage
FROM queries
GROUP BY query_name
HAVING query_name is not null