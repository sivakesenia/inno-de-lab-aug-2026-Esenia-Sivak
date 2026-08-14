-- 1 subpoint: create user hr_user
CREATE USER hr_user WITH PASSWORD 'hr_user123';
-- 2 subpoint: grant right to select (i tried with role creating)
CREATE ROLE select_employees_editor;
GRANT SELECT ON Employees TO select_employees_editor;
GRANT select_employees_editor TO hr_user;
-- 3 subpoint:grant rights to insert and update (without creating role)
GRANT UPDATE, INSERT ON Employees TO hr_user;
-- Optional for serial: GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;
-- but i just wrote id, you can see it in the screenshot
