-- USER TABLE
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at DATE
);
INSERT INTO users(user_id,name, email)
VALUES
(1,'Rojen','rojen@gmail.com'),
(2,'Sien','neis@gmail.com');

-- CATEGORIES TABLE
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50)
    
);
INSERT INTO categories(category_name)
VALUES
('Food'),
('Transport'),
('Shopping'),
('Entertainment'),
('Bills'),
('Health'),
('Education');

-- EXPENSE TABLE
CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    expense_date DATE,
    payment_method VARCHAR(50),
    description VARCHAR(255),

    FOREIGN KEY(user_id)
    REFERENCES users(user_id),

    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)
);
INSERT INTO expenses
(user_id,category_id,amount,expense_date,payment_method,description)
VALUES
(1,1,450,'2026-06-01','Cash','Lunch'),
(1,2,100,'2026-06-02','Cash','Bus fare'),
(1,3,2500,'2026-06-03','Card','Shoes'),
(1,4,800,'2026-06-05','Card','Movie'),
(1,5,1500,'2026-06-07','Online','Internet bill'),
(1,6,700,'2026-06-10','Cash','Medicine'),
(1,7,1200,'2026-06-12','Online','Course'),
(1,1,900,'2026-06-15','Card','Restaurant'),
(1,3,3000,'2026-06-18','Card','Clothes'),
(1,2,300,'2026-06-20','Cash','Taxi');
       
-- INCOME TABLE
CREATE TABLE income (
    income_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount DECIMAL(10,2),
    income_date DATE,
    source VARCHAR(100),
    
    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);
INSERT INTO income
(user_id,amount,income_date,source)
VALUES(1,30000,'2026-06-01','Salary'),
(1,5000,'2026-06-15','Freelance');

-- BUDGET TABLE
CREATE TABLE budgets (
    budget_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_id INT,
    monthly_limit DECIMAL(10,2),

    FOREIGN KEY(user_id)
    REFERENCES users(user_id),

    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)
);
INSERT INTO budgets
(user_id,category_id,monthly_limit)
VALUES(1,1,5000),
(1,2,2000),
(1,3,8000),
(1,4,3000),
(1,5,3000);

SELECT *
FROM users;

SELECT *
FROM expenses;


SELECT SUM(amount) AS total_expense
FROM expenses;

-- CATEGORY-wise spending
SELECT c.category_name, SUM(e.amount) AS total
FROM expenses e JOIN categories c ON e.category_id = c.category_id
GROUP BY c.category_name;

-- SAVING(REMAINING MONEY)
SELECT (
SELECT SUM(amount) FROM income) -
(SELECT SUM(amount) FROM expenses)
AS savings;
