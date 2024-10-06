SELECT round(count(case when DATEDIFF(a1.event_date, a2.event_date) = -1 then 1 end) / (SELECT count(DISTINCT(player_id)) FROM activity),2) as fraction  
FROM activity as a1
JOIN activity as a2 ON a1.player_id = a2.player_id
WHERE (a1.player_id, a1.event_date) in 
(
    select player_id, min(event_date)
    from activity
    group by player_id
)

