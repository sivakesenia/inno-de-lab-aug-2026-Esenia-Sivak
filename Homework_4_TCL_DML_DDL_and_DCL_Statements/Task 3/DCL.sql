-- 1 subpoint: create user hr_user
CREATE USER hr_user WITH PASSWORD 'hr_user123';
-- 2 subpoint: grant right to select (without creating role creating)
GRANT SELECT ON Employees TO hr_user;
-- 3 subpoint:grant rights to insert and update (without creating role)
GRANT UPDATE, INSERT ON Employees TO hr_user;
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;

