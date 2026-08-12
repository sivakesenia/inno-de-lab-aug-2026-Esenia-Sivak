-- select customers from the USA older than 25 y. o.
SELECT
	first_name,
	last_name,
	age,
	country
FROM
	Customers
WHERE
	country = 'USA'
	and age > 25
