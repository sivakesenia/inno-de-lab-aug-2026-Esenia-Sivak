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
WHERE e.EmployeeID NOT EXISTS(
    SELECT 1
    FROM EmployeeProjects ep
    WHERE ep.EmployeeId = e.EmployeeID
);
-- 4 subpoint:  transaction with 2 inserts (into tables project and EmployeeProjects)
START TRANSACTION;

WITH new_project AS (
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('Website Creation', 100000.00, '2026-06-15', '2026-12-30')
    RETURNING ProjectID
)

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES
    (1, (SELECT ProjectID FROM new_project), 130),
    (2, (SELECT ProjectID FROM new_project), 135);

COMMIT;
