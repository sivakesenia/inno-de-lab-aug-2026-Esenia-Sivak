-- 1 subpoint: update salary (+10%) for all employees
UPDATE Employees 
SET salary = salary + salary * 0.1
WHERE department = 'HR';
-- 2 subpoint:  update department of the employee with salary > 70000
UPDATE Employees
SET department = 'Senior IT'
WHERE EmployeeID = (
    SELECT EmployeeID
    FROM Employees
    WHERE salary > 70000.00
    LIMIT 1
);
-- 3 subpoint: delete employees withoot projects
DELETE FROM Employees e
WHERE e.EmployeeID NOT IN (
    SELECT EmployeeId 
    FROM EmployeeProjects 
    WHERE EmployeeId IS NOT NULL
);
-- 4 subpoint:  transaction with 2 inserts (into tables project and EmployeeProjects)
START TRANSACTION;
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) VALUES
('Website Creation', 100000.00, '2026-06-15', '2026-12-30');
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked) VALUES
(1, 4, 130),
(2, 4, 135);
COMMIT;


