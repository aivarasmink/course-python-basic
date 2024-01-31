DROP TABLE customer
CREATE TABLE IF NOT EXISTS customer (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL
);

DROP TABLE product
CREATE TABLE IF NOT EXISTS product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR(50) NOT NULL,
price DECIMAL(10,2) NOT NULL
);

DROP TABLE bill
CREATE TABLE IF NOT EXISTS bill (
id INTEGER PRIMARY KEY AUTOINCREMENT,
purchase_time DATETIME NOT NULL,
cashier_id INTEGER NOT NULL,
customer_id INTEGER REFERENCES customer(id)
);

DROP TABLE BILL_LINE
CREATE TABLE IF NOT EXISTS bill_line (
id INTEGER PRIMARY KEY AUTOINCREMENT,
bill_id INTEGER REFERENCES bill(id),
product_id INTEGER REFERENCES product(id),
quantity DECIMAL(10,2)
);


--kiekviena sąskaitos eilutė
SELECT bill_line.id, product.product_name, bill_line.quantity AS product_name, product.price,
       bill_line.quantity * product.price AS total, 
       bill.purchase_time, customer.first_name AS customer_first_name, customer.last_name AS customer_last_name
FROM bill_line
JOIN product ON bill_line.product_id = product.id
JOIN bill ON bill_line.bill_id = bill.id
JOIN customer ON bill.customer_id = customer.id 
ORDER BY purchase_time;

-- Parduotų produktų kiekis
SELECT product.id, product.product_name, SUM(bill_line.quantity) AS total_sold
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_sold DESC;

--Produktų apyvartos
SELECT product.id, product.product_name, SUM(product.price * bill_line.quantity) AS total_revenue
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_revenue DESC;

--Daugiausiai nupirkę klientai
SELECT customer.id, customer.first_name, customer.last_name, SUM(product.price * bill_line.quantity) AS total_spent
FROM customer
JOIN bill ON customer.id = bill.customer_id
JOIN bill_line ON bill.id = bill_line.bill_id
LEFT JOIN product ON bill_line.product_id = product.id
GROUP BY customer.id
ORDER BY total_spent DESC

--Didžiausia sąskaita
SELECT bill.id, bill.purchase_time, customer.first_name AS customer_first_name, customer.last_name AS customer_last_name,
       SUM(product.price * bill_line.quantity) AS total_amount
FROM bill
JOIN customer ON bill.customer_id = customer.id
JOIN bill_line ON bill.id = bill_line.bill_id
JOIN product ON bill_line.product_id = product.id
GROUP BY bill.id
ORDER BY total_amount DESC

--Konkrečios sąskaitos peržiūra
SELECT bill_line.id, product.product_name, bill_line.quantity AS quantity, product.price,
       bill_line.quantity * product.price AS total_amount,
       bill.purchase_time, customer.first_name, customer.last_name      
FROM bill_line
JOIN product ON bill_line.product_id = product.id
JOIN bill ON bill_line.bill_id = bill.id
JOIN customer ON bill.customer_id = customer.id
WHERE bill.id = 9