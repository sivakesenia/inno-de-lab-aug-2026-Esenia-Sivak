-- 1 subpoint: insert 2 new employees into table Employees (except IT department)
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Esenia', 'Sivak', 'Finance', 52000.00),
('Nick', 'Zhezl', 'HR', 72000.00);
-- 2 subpoint: select all employees from table Employees
SELECT * FROM Employees;
-- 3 subpoint: select employees'  FirstName and LastName from IT department
SELECT
	FirstName,
	LastName
FROM
	Employees
WHERE
	department = 'IT';
-- 4 subpoint: update Alice Smith's salary to 65000.00
UPDATE
    Employees
SET
    Salary = 65000.00
WHERE
	FirstName = 'Alice' AND LastName = 'Smith';
-- 5 subpoint:  delete 'Eve Davis'
DELETE FROM
	Employees
WHERE
	FirstName = 'Eve'
	AND LastName = 'Davis';
-- 6 subpoint:  check
SELECT * FROM Employees;