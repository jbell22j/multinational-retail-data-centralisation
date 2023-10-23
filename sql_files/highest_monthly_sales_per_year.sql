SELECT MAX(total_sales) AS total_sales,
	   year
FROM (SELECT SUM(product_price*product_quantity) AS total_sales,
	   month,
	   year
FROM dim_products
INNER JOIN orders_table
ON orders_table.product_code = dim_products.product_code
INNER JOIN dim_date_times
ON dim_date_times.date_uuid = orders_table.date_uuid
GROUP BY month,
	 year)
GROUP BY year;

	   
	   

