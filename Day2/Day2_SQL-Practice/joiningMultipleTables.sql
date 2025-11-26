/*select top 5 * from Sales.Customers
select top 5 * from Sales.Products
select top 5 *  from Sales.Employees
select top 5 * from Sales.Orders*/
select o.OrderID,c.FirstName,p.Product,o.Sales,p.Price,e.FirstName 
from Sales.Orders as o 
left join Sales.Employees as e on SalesPersonID=EmployeeID 
left join sales.Products as p on o.ProductID=p.ProductID 
left join sales.Customers as c on o.CustomerID= c.CustomerID
