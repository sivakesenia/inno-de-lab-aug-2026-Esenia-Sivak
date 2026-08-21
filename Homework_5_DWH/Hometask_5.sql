-- calculate total revenue and number of tickets sold
SELECT
    COUNT(*) AS tickets_sold,
    SUM(ticket_price) AS full_sales,
    SUM(discount_amount) AS total_discounts,
    SUM(total_revenue) AS total_revenue,
    AVG(total_revenue) AS average_revenue_per_ticket
FROM fact_ticket_sales;

-- Dynamics by month
SELECT
    d.year,
    d.month,
    COUNT(*) AS tickets_sold,
    SUM(f.total_revenue) AS total_revenue
FROM fact_ticket_sales f
JOIN dim_date d
    ON f.date_sk = d.date_sk
GROUP BY
    d.year,
    d.month
ORDER BY
    d.year,
    d.month;

-- the most profitable events
SELECT
    e.title,
    COUNT(*) AS tickets_sold,
    SUM(f.total_revenue) AS total_revenue
FROM fact_ticket_sales f
JOIN dim_event e
    ON f.event_sk = e.event_sk
GROUP BY
    e.title
ORDER BY
    total_revenue DESC;

-- Compare performance categories
SELECT
    ec.category_name,
    COUNT(*) AS tickets_sold,
    SUM(f.total_revenue) AS total_revenue,
    AVG(f.total_revenue) AS average_revenue_per_ticket
FROM fact_ticket_sales f
JOIN dim_event e ON f.event_sk = e.event_sk
JOIN dim_event_category ec ON e.event_category_sk = ec.event_category_sk
GROUP BY
    ec.category_name
ORDER BY
    total_revenue DESC;

-- Analyze from which country people buy tickets the most often
SELECT
    ct.country_name,
    COUNT(*) AS tickets_sold,
    COUNT(DISTINCT f.customer_sk) AS unique_customers,
    SUM(f.total_revenue) AS total_revenue
FROM fact_ticket_sales f
JOIN dim_customer c
    ON f.customer_sk = c.customer_sk
JOIN dim_country ct
    ON c.country_sk = ct.country_sk
GROUP BY
    ct.country_name
ORDER BY
    tickets_sold DESC;
	