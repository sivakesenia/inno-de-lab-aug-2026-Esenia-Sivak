-- 1 subpoint: create table Departments with columns: 
-- DepartmentID (SERIAL PRIMARY KEY), DepartmentName (VARCHAR(50), UNIQUE, NOT NULL), Location (VARCHAR(50)).
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
LOCATION VARCHAR(50)
);
-- 2 subpoint: add new column Email to table Employees:
ALTER TABLE Employees ADD COLUMN Email VARCHAR(100);
--3 subpoint:  fullfill column email for each employee:
UPDATE Employees
SET Email = LOWER(FirstName || LastName || CAST(EmployeeID AS text) || '@gmail.com');
--4 subpoint: add unique constraint to email
ALTER TABLE Employees ADD CONSTRAINT UQ_Email UNIQUE (Email);
-- 5 subpoint: rename table Location to OfficeLocation in table Departments:
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;