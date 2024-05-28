# Write your MySQL query statement below
SELECT p.product_id, IFNULL(round(sum(units*price)/sum(units),2),0) AS average_price
FROM UnitsSold as u
RIGHT JOIN prices as p ON u.product_id = p.product_id AND (u.purchase_date >= p.start_date AND u.purchase_date <= p.end_date)
GROUP BY product_id