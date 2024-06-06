select distinct num ConsecutiveNums
from(
SELECT num,
       LAG(num, 1) OVER (ORDER BY id) AS prev_num,
       LEAD(num, 1) OVER (ORDER BY id) AS next_num
FROM Logs 
) as sub
where num = prev_num and num = next_num


// lag(해당 열, offset) over(기준열) lead도 똑같음.