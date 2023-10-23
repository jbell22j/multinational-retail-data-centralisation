SELECT AVG(next_order::TIME) AS actual_time_taken,
year
FROM(SELECT 
	year,
	LEAD(timestamp, 1) OVER (
		ORDER BY timestamp) AS next_order
FROM 
	dim_date_times
ORDER BY next_order DESC)
GROUP BY year;