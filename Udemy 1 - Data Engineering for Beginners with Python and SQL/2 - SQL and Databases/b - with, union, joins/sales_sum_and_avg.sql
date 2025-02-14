select 
product_category as 'Product Category', 
sum(sales_amount) as 'Total Sales Amount', 
avg(sales_amount) as 'Average Sales Amount'
from sales 
group by product_category
order by 'Total Sales Amount' desc

/*
Sales Analysis
Aim: Find the Total Sales and Average Sales per Product Category

In this SQL coding exercise, you will work with a database table called sales. Your task is to write a SELECT query to analyze sales data and find the total sales amount and average sales amount per product category.

Data Description:

You are provided with a table named sales with the following columns:

sale_id (integer) - Primary Key

product_category (varchar(50))

sales_amount (decimal(10, 2))

Instructions:

Write a SQL SELECT query that retrieves the following information:

Product category

Total sales amount for each product category

Average sales amount for each product category

Group the results by product category.

Sort the results in descending order based on total sales amount.

Product Category  | Total Sales Amount | Average Sales Amount
-------------------------------------------------------------
Electronics       | 50000.00           | 250.00
Clothing          | 35000.00           | 175.00
Books             | 28000.00           | 140.00
*/