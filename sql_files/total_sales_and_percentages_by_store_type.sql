SELECT store_type,
	   SUM(product_price*product_quantity) AS total_sales,
	   (SUM(product_price*product_quantity) * 100 )/SUM(SUM(product_price*product_quantity)) OVER () AS total_percentage
FROM dim_products
INNER JOIN orders_table
ON orders_table.product_code = dim_products.product_code
INNER JOIN dim_store_details
ON dim_store_details.store_code = orders_table.store_code
GROUP BY store_type
ORDER BY total_sales DESC;
	   
	   

