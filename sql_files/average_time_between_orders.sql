SELECT AVG(time_till_next) AS actual_time_taken,
		year
FROM 
(SELECT timestamp-next_order AS time_till_next,
year
FROM 
(SELECT 
    timestamp,
	LEAD(timestamp,1) OVER (ORDER BY timestamp DESC) AS next_order,
	year
FROM
(SELECT 
	TO_TIMESTAMP(timestamp,'HH24:MI:SS DD/MM/YYYY') AS timestamp,
	year
FROM
(WITH datetime_CTE AS (SELECT CAST(timestamp AS VARCHAR),
CONCAT(day,'/',month,'/',year) AS date,
year
FROM dim_date_times)
SELECT CONCAT(timestamp,' ',date) AS timestamp ,year
FROM datetime_CTE))))
GROUP BY year
ORDER BY actual_time_taken DESC;
