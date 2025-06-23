
-- 1. Remove rows with missing amount
SELECT * FROM orders WHERE amount IS NOT NULL;

-- 2. Remove invalid status
SELECT * FROM orders WHERE status != 'invalid';

-- 3. Join customers with valid orders
SELECT 
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.amount
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
WHERE 
    o.status = 'completed';

-- 4. Total orders per customer
SELECT 
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_spent
FROM 
    orders
WHERE 
    status = 'completed'
GROUP BY 
    customer_id;
