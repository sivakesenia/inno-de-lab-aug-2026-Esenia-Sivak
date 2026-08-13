-- select the list of orders with customer's name
SELECT
	c.first_name,
	c.last_name,
	o.item,
	o.amount
FROM
	Orders AS o
-- i used inner join cuz the task requires the list of orders TOGETHER with the customer's name
INNER JOIN Customers AS c ON
	o.customer_id = c.customer_id