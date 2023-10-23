SELECT SUM(product_price*product_quantity) AS total_sales,
           month
FROM (SELECT product_price,
	 product_quantity,
	 date_uuid
	 FROM orders_table
	 INNER JOIN dim_products
	 ON dim_products.product_code = orders_table.product_code) AS product_orders
INNER JOIN dim_date_times
ON dim_date_times.date_uuid = product_orders.date_uuid
GROUP BY month
LIMIT 6;

