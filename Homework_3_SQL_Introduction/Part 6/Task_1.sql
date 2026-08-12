-- for each order add column with customer's orders sum 
SELECT
	o.order_id,
	c.customer_id,
	o.item,
	o.amount,
	SUM(amount) OVER( PARTITION BY c.customer_id ) AS total_by_customer
FROM
	orders o
JOIN customers c ON
	o.customer_id = c.customer_id
ORDER BY c.customer_id 
