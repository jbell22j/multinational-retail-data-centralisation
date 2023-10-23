SELECT SUM(product_quantity*product_price) AS total_sales,
		   country_code,
		   store_type
FROM dim_store_details
INNER JOIN orders_table
ON dim_store_details.store_code = orders_table.store_code
INNER JOIN dim_products
ON dim_products.product_code = orders_table.product_code
WHERE country_code = 'DE'
GROUP BY country_code,
		 store_type
ORDER BY total_sales ASC;


	   
	   

