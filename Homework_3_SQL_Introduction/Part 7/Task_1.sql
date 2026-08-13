SELECT
-- fullname is made with the help of concatanation
	c.first_name || ' ' || c.last_name AS fullname,
	c.country,
--count orders by customer_id
	COUNT(*) AS total_orders,
-- sum amount by customer_id
	SUM(amount) AS total_amount
FROM
	Customers c
JOIN Orders o ON
	c.customer_id = o.customer_id
GROUP BY
	c.customer_id 
HAVING
-- at least 2 orders
	COUNT(*) >= 2
-- at least 1 shipping has status 'Delivered'
	AND EXISTS (
	SELECT
		1
	FROM
		shippings s
	WHERE s.customer  = c.customer_id
	AND
		s.status  = 'Delivered' )
