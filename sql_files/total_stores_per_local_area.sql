SELECT locality,
	   COUNT(locality) AS total_number_of_stores
FROM dim_store_details
GROUP BY locality
ORDER BY total_number_of_stores DESC
LIMIT 7;