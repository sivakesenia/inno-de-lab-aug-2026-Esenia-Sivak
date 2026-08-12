-- select the list of customers selected by descending order
SELECT
	order_id,
	customer_id,
	item,
	amount,
	SUM(amount) OVER() AS total_by_customer
FROM
	orders o
JOIN customers c ON
	o.customer_id = c.customer_id
