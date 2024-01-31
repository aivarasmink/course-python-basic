--most sold products
SELECT product_id, SUM(quantity) AS total_sold
FROM bill_line
GROUP BY product_id
ORDER BY total_sold DESC
LIMIT 10;

--highest product revenue
SELECT product_id, SUM(quantity * unit_price) AS total_revenue
FROM bill_line
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;

--best customers
SELECT customer_id, SUM(quantity * unit_price) AS total_revenue
FROM bill_line
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;

--largest bill
SELECT customer_id, SUM(quantity * unit_price) AS total_revenue
FROM bill_line
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 1;