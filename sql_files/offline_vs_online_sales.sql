SELECT SUM(product_quantity) AS product_quantity_count,
	   COUNT(user_uuid) AS number_of_sales,
	   CASE
	   WHEN store_code LIKE 'WEB%' THEN 'Web'
	   ELSE 'Offline' END AS location
FROM orders_table
GROUP BY location;

