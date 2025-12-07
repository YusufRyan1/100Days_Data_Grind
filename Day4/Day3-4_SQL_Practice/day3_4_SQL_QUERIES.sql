/*
Exercise Set 1 – Joins

1.Select all employees along with their department name (INNER JOIN).

2.Select all employees including those without a department (LEFT JOIN).

3.Find departments with no employees (anti-join / NOT EXISTS).

4.Do a SELF JOIN to find employees in the same department.
*/
select * from employees as e inner join departments as d on e.dep_id=d.dep_id
select * from employees as e left join departments as d on e.dep_id=d.dep_id
select * from departments as d left join employees as e on e.dep_id=d.dep_id where e.dep_id is null
select * from employees as e inner join employees as eo on e.dep_id=eo.dep_id
select * from employees as e inner join employees as eo on e.dep_id=eo.dep_id where e.name !=eo.name

/*Exercise Set 2 – Aggregates & HAVING

1.Find the average salary per department.

2.Show only departments where average salary > 5000 (HAVING).

3.Count the number of employees per department.*/

select d.dep_name,avg(salary) from employees as e join departments as d on e.dep_id=d.dep_id group by d.dep_name
select d.dep_name,avg(salary) from employees as e join departments as d on e.dep_id=d.dep_id group by d.dep_name having avg(salary)>5000
select d.dep_name,count(emp_id) from employees as e join departments as d on e.dep_id=d.dep_id group by d.dep_name

/*
Exercise Set 3 – Updates & Deletes

1.Increase salary of all employees in IT by 10%.

2.Delete employees in the HR department (practice!).

3.Move employees with salary < 5000 to Sales (subquery update).
*/
select * from employees
update employees 
set salary=salary *1.1 where dep_id = (
								select distinct  e.dep_id
								from employees e left join departments d on e.dep_id=d.dep_id
								where dep_name='IT')

delete from employees where dep_id = (
								select distinct  e.dep_id
								from employees e left join departments d on e.dep_id=d.dep_id
								where dep_name='HR')

update employees 
set dep_id = (
				select distinct  e.dep_id
				from employees e left join departments d on e.dep_id=d.dep_id
				where dep_name='Sales') where salary <5000



/* 
Exercise Set 4 – Subqueries

List employees whose salary is greater than average salary.

Find the department with the highest total salary
*/

select
*
from employees where employees.salary >(select avg(salary) from employees)

SELECT d.dep_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dep_id = d.dep_id
GROUP BY d.dep_name
HAVING SUM(e.salary) = (
    SELECT MAX(total_sal)
    FROM (
        SELECT SUM(salary) AS total_sal
        FROM employees
        GROUP BY dep_id
    ) t
);

 -- Find the second highest salary in the company
 SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
