CREATE TABLE student (
    id INT PRIMARY KEY,
    name NVARCHAR(50),
    address NVARCHAR(100),
    score INT
);

INSERT INTO student (id, name, address, score) VALUES
(1, 'Ahmed', 'Cairo', 95),
(2, 'Fatima', 'Alexandria', 88),
(3, 'Youssef', 'Giza', 76),
(4, 'Mona', 'Cairo', 82),
(5, 'Omar', 'Alexandria', 90);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name NVARCHAR(50),
    section NVARCHAR(50),
    price DECIMAL(5,2)
);

INSERT INTO products (id, name, section, price) VALUES
(1, 'Milk', 'Dairy', 2.5),
(2, 'Cheese', 'Dairy', 3.0),
(3, 'Bread', 'Bakery', 1.2),
(4, 'Cake', 'Bakery', 4.0),
(5, 'Apple', 'Fruits', 0.5),
(6, 'Banana', 'Fruits', 0.3);

-- Total number of products per section
SELECT section, COUNT(*) AS total_products
FROM products
GROUP BY section;

-- Average price per section
SELECT section, AVG(price) AS avg_price
FROM products
GROUP BY section;

-- Sections with avg price > 2
SELECT section, AVG(price) AS avg_price
FROM products
GROUP BY section
HAVING AVG(price) > 2;

-- Top 2 most expensive products
SELECT TOP 2 * FROM products
ORDER BY price DESC;

-- Bakery products with price > 3
SELECT * FROM products
WHERE section = 'Bakery' AND price > 3;
