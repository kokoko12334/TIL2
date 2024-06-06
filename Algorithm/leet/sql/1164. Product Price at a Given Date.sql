# Write your MySQL query statement below
WITH latest_price AS (
    SELECT product_id, new_price
    FROM products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date)
        FROM products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
)
select distinct p.product_id, coalesce(lp.new_price, 10) as price
from products p
left join latest_price as lp on p.product_id = lp.product_id
order by p.product_id
