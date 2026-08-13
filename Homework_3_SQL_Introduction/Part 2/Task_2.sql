-- select the list of shippings with status and customer's name
SELECT
	s.status,
	c.first_name,
	c.last_name
FROM
	shippings AS s
INNER JOIN Customers AS c ON
	s.customer = c.customer_id