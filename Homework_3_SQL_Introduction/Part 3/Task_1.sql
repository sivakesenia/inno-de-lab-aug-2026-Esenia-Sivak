-- select the count of customers in each country
SELECT
	c.country,
	COUNT(*) AS count
FROM
	Customers AS c
GROUP BY
	c.country