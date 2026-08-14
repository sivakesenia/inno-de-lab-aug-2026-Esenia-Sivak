-- 1 subpoint: select ProjectName of all projects where Bob Johnson worked more than 150 h
SELECT
	projectname
FROM
	projects p
JOIN employeeprojects ep ON
	p.projectid = ep.projectid
JOIN employees e ON
	ep.employeeid = e.employeeid
WHERE
	e.firstname = 'Bob'
	AND e.lastname = 'Johnson'
	AND ep.hoursworked > 150;

-- variant with subquery
SELECT
	p.ProjectName
FROM
	Projects p
WHERE
	p.ProjectID IN (
	SELECT
		ep.ProjectID
	FROM
		EmployeeProjects ep
	JOIN Employees e ON
		ep.EmployeeID = e.EmployeeID
	WHERE
		e.FirstName = 'Bob'
		AND e.LastName = 'Johnson'
		AND ep.HoursWorked > 150
);

-- 2 subpoint: increase Budget by 10% for projects with at least one IT employee assigned
UPDATE
	Projects p
SET
	budget = budget * 1.1
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects ep
    JOIN Employees e ON ep.EmployeeID = e.EmployeeID
    WHERE p.ProjectID = ep.ProjectID
      AND e.Department = 'IT'
);

-- 3 subpoint: set EndDate to one year after StartDate for projects with no EndDate
UPDATE Projects p
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

-- 4 subpoint: insert new employee and assign them to Website Redesign project within one transaction, using RETURNING
START TRANSACTION;

WITH new_employee AS (
    INSERT INTO Employees (FirstName, LastName, Email, Department, Salary)
    VALUES ('Jenny', 'Smith', 'jennysmith@gmail.com', 'IT', 75000.00)
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
    ne.EmployeeID,
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),
    80
FROM new_employee ne;

COMMIT;