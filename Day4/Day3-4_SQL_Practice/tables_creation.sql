-- Create Practice DB if not exists
IF DB_ID('PracticeDB') IS NULL
    CREATE DATABASE PracticeDB;
GO
USE PracticeDB;
GO

-- Employee table (recreate safe)
IF OBJECT_ID('dbo.employee','U') IS NOT NULL DROP TABLE dbo.employee;
CREATE TABLE dbo.employee (
    emp_id INT PRIMARY KEY,
    emp_name NVARCHAR(100) NOT NULL,
    emp_age INT NULL,
    salary DECIMAL(10,2) NULL,
    hire_date DATE NULL,
    dep_id INT NULL
);
GO

-- Departments table
IF OBJECT_ID('dbo.departments','U') IS NOT NULL DROP TABLE dbo.departments;
CREATE TABLE dbo.departments (
    dep_id INT PRIMARY KEY,
    dep_name NVARCHAR(100) NOT NULL
);
GO

-- Sales table (for join practice)
IF OBJECT_ID('dbo.sales','U') IS NOT NULL DROP TABLE dbo.sales;
CREATE TABLE dbo.sales (
    sale_id INT PRIMARY KEY,
    emp_id INT NULL,
    product NVARCHAR(100),
    amount DECIMAL(10,2),
    sale_date DATE
);
GO
