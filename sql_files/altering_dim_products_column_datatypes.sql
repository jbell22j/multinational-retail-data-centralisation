ALTER TABLE dim_products ALTER available TYPE boolean
USING CASE available WHEN 'Available' THEN TRUE WHEN 'Removed'  THEN FALSE END;
ALTER TABLE dim_products ALTER product_price TYPE FLOAT USING product_price::double precision;
ALTER TABLE dim_products ALTER weight TYPE FLOAT;
ALTER TABLE dim_products ALTER date_added TYPE DATE USING date_added::date;
ALTER TABLE dim_products ALTER uuid TYPE UUID USING uuid::uuid;
ALTER TABLE dim_products ALTER weight_class TYPE VARCHAR(12);
ALTER TABLE dim_products ALTER "EAN" TYPE VARCHAR(18);
ALTER TABLE dim_products ALTER product_price TYPE VARCHAR(20);
