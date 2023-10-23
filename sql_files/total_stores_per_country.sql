SELECT country_code,
	   COUNT(country_code) AS total_number_of_stores
FROM dim_store_details
GROUP BY country_code
ORDER BY total_number_of_stores DESC;