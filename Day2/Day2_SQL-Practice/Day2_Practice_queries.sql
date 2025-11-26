
-- PART 1 — DDL (CREATE / ALTER / DROP)
-- Task 1: Create a table called employees:

create table employee (
emp_id  int not null primary key,
emp_name varchar(50) not null,
emp_age int not null ,
department varchar(50) ,
salary int 
)

-- Task 2: Add a new column

alter table employee 
add hire_date date

-- Task 3: Modify a column
alter table employee
alter column salary decimal(10,2)

-- Task 4: Drop a column
alter table employee
drop column emp_age 

-- PART 2 — DML (INSERT, UPDATE, DELETE)
-- Task 5: Insert 5 employees

insert into employee  (emp_id,emp_name,department,salary,hire_date)
values (1,'Sarah Ahmed','Marketing' ,4200,'2022-03-15'),
(2,'Omar Youssef','IT',6800,'2021-11-02'),
(3,'Mona El-Sayed','HR',3900,'2023-06-10'),
(4,'Ali Hassan','Finance',9500,'2019-01-20'),
(5,'Nour Khaled','Sales',5200,'2020-08-07')

-- Task 6: Update salary
update employee
set salary = salary + (.10*salary)
where department='IT'


-- Task 7: Delete

 delete from employee where salary <5000

-- PART 3 — WHERE Conditions
--Task 8: Select all employees with salary between 7000 and 12000
 select * from employee where salary between 7000 and 12000

--Task 9: Find employees whose name starts with 'A'
select * from employee where emp_name like 'A%'

--Task 10: Find employees hired after 2020
select * from employee where hire_date>'2020-01-01'

-- PART 4 — JOINS
create table departments
(
dep_id int primary key not null,
dep_name varchar(50)
)

insert into departments (dep_id,dep_name)
values (1, 'Marketing'),
(2, 'IT'),
(3, 'HR'),
(4, 'Finance'),
(5,'sales')


alter table employee 
add dep_id int

update employee set dep_id =1 where department='Marketing'
update employee set dep_id =2 where department='IT'
update employee set dep_id =3 where department='HR'
update employee set dep_id =4 where department='Finance'
update employee set dep_id =5 where department='sales'
select * from employee

alter table employee
drop column department

--Task 11: INNER JOIN
select emp_id,emp_name,salary,dep_name from employee as e inner join departments as d on e.dep_id=d.dep_id

--Task 12: LEFT JOIN
select * from employee as e left join departments as d on e.dep_id=d.dep_id

--Task 13: Aggregation with JOIN
select avg(salary),dep_name 
from employee as e full join departments as d on e.dep_id=d.dep_id 
group by dep_name

