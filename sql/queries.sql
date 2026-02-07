

-- Total sales by product
SELECT p.product_name, SUM(s.total_price) AS revenue
FROM sales_fact s
JOIN product_dim p ON s.product_id = p.product_id
GROUP BY p.product_name;

-- Sales by month
SELECT d.year, d.month, SUM(s.total_price) AS revenue
FROM sales_fact s
JOIN date_dim d ON s.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- Sales by country
SELECT c.country, SUM(s.total_price) AS revenue
FROM sales_fact s
JOIN customer_dim c ON s.customer_id = c.customer_id
GROUP BY c.country;

-- Total profit
SELECT SUM(profit) AS total_profit FROM sales_fact;