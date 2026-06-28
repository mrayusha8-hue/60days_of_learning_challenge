SELECT * FROM employees;
SELECT * FROM orders;
SELECT * FROM customers;


-- Display all records from employees table
SELECT * FROM employees;

-- Display only employee names and salaries
SELECT name, salary FROM employees;

-- Display unique departments from employees
SELECT DISTINCT department FROM employees;

-- Display customers from Kathmandu city
SELECT * FROM customers WHERE city = 'Kathmandu';

-- Display orders with amount greater than 5000
SELECT * FROM orders WHERE amount > 5000;


-- Filtering (WHERE)

-- Find employees whose salary is greater than 60000
SELECT * FROM employees WHERE salary > 60000;

-- Find employees who work in the IT department
SELECT * FROM employees WHERE department = 'IT';

-- Find employees whose salary is between 40000 and 70000
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 70000;

-- Find customers whose names start with "A"
SELECT * FROM customers WHERE name LIKE 'A%';

-- Find all completed orders
SELECT * FROM orders WHERE status = 'Completed';


-- Sorting (ORDER BY)

-- Display employees sorted by highest salary first
SELECT * FROM employees ORDER BY salary DESC;

-- Display customers alphabetically by name
SELECT * FROM customers ORDER BY name ASC;

-- Display orders from highest amount to lowest
SELECT * FROM orders ORDER BY amount DESC;


-- Aggregate Functions

-- Count total employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Find the maximum salary
SELECT MAX(salary) AS max_salary FROM employees;

-- Find the minimum salary
SELECT MIN(salary) AS min_salary FROM employees;

-- Find average employee salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- Find total order amount
SELECT SUM(amount) AS total_order_amount FROM orders;

-- Count total number of orders
SELECT COUNT(*) AS total_orders FROM orders;


-- GROUP BY

-- Find average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Find number of employees in each department
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;

-- Find total sales by customer
SELECT customer_id, SUM(amount) AS total_sales
FROM orders
GROUP BY customer_id;

-- Find total completed sales
SELECT SUM(amount) AS completed_sales
FROM orders
WHERE status = 'Completed';

-- Find number of orders by status
SELECT status, COUNT(*) AS num_orders
FROM orders
GROUP BY status;


-- HAVING
-- Find departments where average salary is above 50000
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- Find customers who spent more than 10000
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 10000;

-- Find cities having more than 5 customers
SELECT city, COUNT(*) AS num_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 5;
