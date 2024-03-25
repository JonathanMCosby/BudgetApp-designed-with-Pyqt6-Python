CREATE SCHEMA budgetProgram;
CREATE TABLE budgetProgram.user (
user_id INT AUTO_INCREMENT PRIMARY KEY,
user_name VARCHAR(40),
first_name VARCHAR(40),
last_name VARCHAR(40),
password VARCHAR(40)
);
CREATE TABLE budgetProgram.table (
entry_id int AUTO_INCREMENT PRIMARY KEY,
user_name VARCHAR(40),
primary_income DECIMAL(10,2),
side_income DECIMAL(10,2),
total_income DECIMAL(10,2),
needs DECIMAL (10,2),
wants DECIMAL (10,2),
save DECIMAL (10,2),
date DATETIME DEFAULT CURRENT_TIMESTAMP NULL
);
DROP TABLE budgetProgram.table;