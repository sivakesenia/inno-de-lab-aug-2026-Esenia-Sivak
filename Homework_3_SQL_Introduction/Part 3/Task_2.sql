-- select the count of orders and each item's average amount 
SELECT
	o.item,
	COUNT(*) AS count,
-- rounded to 2 decimal places as in examples's result
	ROUND(AVG(amount), 2) AS avg_amount
FROM
	Orders AS o
GROUP BY
	o.item