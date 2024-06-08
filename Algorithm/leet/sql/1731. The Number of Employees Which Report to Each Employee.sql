# Write your MySQL query statement below
with cte as(
select reports_to, count(reports_to) reports_count, round(avg(age)) average_age
from employees
where reports_to is not null
group by reports_to
)

select c.reports_to as employee_id, e.name, reports_count, average_age
from employees as e
right join cte as c on c.reports_to = e.employee_id
order by employee_id