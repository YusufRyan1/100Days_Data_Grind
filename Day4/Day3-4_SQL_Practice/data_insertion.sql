-- Seed departments
INSERT INTO dbo.departments (dep_id, dep_name) VALUES
(1, 'Marketing'), (2, 'IT'), (3, 'HR'), (4, 'Finance'), (5, 'Sales');

-- Seed employees
INSERT INTO dbo.employee (emp_id, emp_name, emp_age, salary, hire_date, dep_id) VALUES
(1, 'Sarah Ahmed', 29, 4200, '2022-03-15', 1),
(2, 'Omar Youssef', 31, 6800, '2021-11-02', 2),
(3, 'Mona El-Sayed', 28, 3900, '2023-06-10', 3),
(4, 'Ali Hassan', 35, 9500, '2019-01-20', 4),
(5, 'Nour Khaled', 27, 5200, '2020-08-07', 5),
(6, 'Kareem Samir', 30, 7200, '2020-09-15', 2),
(7, 'Laila Amin', 26, 4500, '2021-04-02', 1),
(8, 'Tamer Omar', 32, 6100, '2018-12-11', 4);

-- Seed sales
INSERT INTO dbo.sales (sale_id, emp_id, product, amount, sale_date) VALUES
(1, 1, 'Milk', 25, '2023-10-01'),
(2, 5, 'Apple', 10, '2023-10-02'),
(3, 2, 'Laptop', 2500, '2023-10-03'),
(4, 6, 'Keyboard', 150, '2023-10-04'),
(5, 2, 'Mouse', 40, '2023-10-05'),
(6, NULL, 'Promotion Voucher', 0, '2023-10-06'); -- sale without emp (to practice outer joins)
