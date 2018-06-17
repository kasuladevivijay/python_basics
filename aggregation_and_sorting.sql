SELECT customers.first_name, customers.last_name, COUNT(purchases.id)
FROM customers
LEFT JOIN purchases
ON customers.id = purchases.id
GROUP BY customers.id

SELECT customers.first_name, customers.last_name, SUM(items.price) AS "total_spent" FROM items
INNER JOIN purchases
ON items.id = purchases.id
RIGHT JOIN customers
ON purchases.customer_id = customers.id
GROUP BY customers.id
ORDER BY total_spent DESC

SELECT * FROM customers 
LEFT JOIN purchases
ON customers.id = purchases.customer_id