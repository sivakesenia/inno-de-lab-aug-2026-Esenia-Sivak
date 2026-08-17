-- 1 subpoint: create func CalculateAnnualBonus
CREATE FUNCTION CalculateAnnualBonus(employeer_id INTEGER, salary DECIMAL)
RETURNS DECIMAL
LANGUAGE plpgsql
AS $$
DECLARE
	bonus DECIMAL;
BEGIN
	bonus := salary * 0.1;
	RETURN bonus;
END;
$$;
-- 2 subpoint: use the function
SELECT 
    FirstName,
    LastName,
    CalculateAnnualBonus(EmployeeID, Salary) AS bonus
FROM Employees;
-- 3 supoint: create view
CREATE VIEW IT_Department_View AS 
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM Employees
WHERE Department = 'IT';
-- 4 subpoint: use the view
SELECT * FROM IT_Department_View;

