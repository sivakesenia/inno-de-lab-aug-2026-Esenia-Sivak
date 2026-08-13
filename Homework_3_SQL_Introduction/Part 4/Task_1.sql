-- select the list of customers selected by descending order
SELECT
    c.first_name,
    c.age
FROM
    customers c
ORDER BY
    c.age DESC
