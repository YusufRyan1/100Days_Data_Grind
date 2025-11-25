-- 1.Select all columns from the student table
select * from student

-- 2.Select only name and score.
select name, score from student

-- 3.Select students who live in Cairo
select * from student where address='Cairo'

-- 4.Select students with score > 85.
select * from student where score >85

-- 5.Select students whose name starts with “A”.
select * from student where name like 'A%'

-- 6.Count how many students live in each city.
select address,count(name) from student group by address

-- 7.Find the average score of students in each city.
select address,avg(score) from student group by address

-- 8.Find cities where the average score > 85.
select address,avg(score) from student group by address having avg(score)>85

-- 9.Show students ordered by score descending.
select * from student order by score desc

-- 10.Show the top 3 students by score.
select top 3 * from student order by score desc

-- 11.Select all products.
select * from products

-- 12.Select name and price of products in the Dairy section.
select name , price from products where section='Dairy'

-- 13.Count how many products are in each section.
select section , count(name) from products group by section

-- 14.Find the average price per section.
select section , avg(price) from products group by section

-- 15.Show products in the Bakery section with price > 3.
select name from products where section='Bakery' and price >3