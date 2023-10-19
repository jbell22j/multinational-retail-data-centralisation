ALTER TABLE dim_products RENAME COLUMN removed TO available;
UPDATE dim_products SET product_price = REPLACE(product_price,'£','');
ALTER TABLE dim_products ADD weight_class VARCHAR(255);
UPDATE dim_products 
SET weight_class =
(SELECT 
CASE
	WHEN weight < 2 THEN 'Light'
	WHEN weight BETWEEN 2 AND 40 THEN 'Mid_Sized'
	WHEN weight BETWEEN 40 AND 140 THEN 'Heavy'
	ELSE 'Truck_Sized'
END);