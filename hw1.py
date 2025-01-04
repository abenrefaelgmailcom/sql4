# 1. הצג את כל הקורסים שיש להם מרצה ואת המרצה של הקורס (INNER JOIN):
SELECT
    Courses.name AS course_name,
    Lecturers.name AS lecturer_name
FROM Courses
INNER JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


# 2. הצג את כל הקורסים (עם ובלי מרצה) ואת המרצה של הקורס (LEFT JOIN):
SELECT
    Courses.name AS course_name,
    Lecturers.name AS lecturer_name
FROM Courses
LEFT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


# 3. הצג את כל המרצים המשובצים לקורס + מרצים שעדיין לא משובצים (RIGHT JOIN):
SELECT
    Courses.name AS course_name,
    Lecturers.name AS lecturer_name
FROM Courses
RIGHT JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


# 4. הצג את כל הקורסים שאין להם מרצה:
SELECT
    Courses.name AS course_name
FROM Courses
WHERE lecturer_id IS NULL;


# 5. הצג את כל המרצים שעדיין לא משובצים לקורס:
SELECT
    Lecturers.name AS lecturer_name
FROM Lecturers
LEFT JOIN Courses ON Lecturers.lecturer_id = Courses.lecturer_id
WHERE Courses.lecturer_id IS NULL;


# 6. הצג את כל הקורסים ואת המרצה של הקורס + קורסים שאין להם מרצה + מרצים שעדיין לא משובצים (FULL JOIN):
SELECT
    Courses.name AS course_name,
    Lecturers.name AS lecturer_name
FROM Courses
FULL OUTER JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id;


# 7. הצג את כל המרצים שעדיין לא משובצים לקורס + הקורסים שאין להם מרצה (FULL JOIN עם בדיקת NULL):
SELECT
    Courses.name AS course_name,
    Lecturers.name AS lecturer_name
FROM Courses
FULL OUTER JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id IS NULL OR Lecturers.lecturer_id IS NULL;


# 8. הצג את כל המרצים שיש בשם שלהם את האות 'i':
SELECT
    name AS lecturer_name
FROM Lecturers
WHERE name LIKE '%i%';


# 9. ספור כמה מרצים יש:
SELECT
    COUNT(*) AS total_lecturers
FROM Lecturers;


10. ספור כמה קורסים יש:
SELECT
    COUNT(*) AS total_courses
FROM Courses;


# 11. הוסף עמודה לטבלת קורסים של שעות שבועיות ועדכן את הערכים:
ALTER TABLE Courses
ADD COLUMN weekly_hours INTEGER;

UPDATE Courses
SET weekly_hours = 4
WHERE course_id IN (1, 2, 3);

UPDATE Courses
SET weekly_hours = 6
WHERE course_id IN (4, 5, 6);

UPDATE Courses
SET weekly_hours = 8
WHERE course_id IN (7, 8, 9, 10);


# 12. הצג כמה קורסים יש לכל ערך של שעות שבועיות:
SELECT
    weekly_hours,
    COUNT(*) AS course_count
FROM Courses
GROUP BY weekly_hours;


# 13. הצג את כל המרצים שמלמדים קורסים של 8 שעות:
SELECT
    Lecturers.name AS lecturer_name
FROM Courses
INNER JOIN Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.weekly_hours = 8;


# 14. מחק את כל הקורסים של 4 שעות שבועיות שאין להם מרצה משובץ:
DELETE FROM Courses
WHERE weekly_hours = 4 AND lecturer_id IS NULL;


# 15. הצג את כל העובדים ואת פרטי המחלקה אליה הם שייכים (INNER JOIN):
SELECT
    Employees.emp_id,
    Employees.name AS employee_name,
    Employees.salary,
    Departments.name AS department_name
FROM Employees
INNER JOIN Departments ON Employees.department_id = Departments.department_id;


# 16. הצג את כל העובדים עם ובלי מחלקה (LEFT JOIN):
SELECT
    Employees.emp_id,
    Employees.name AS employee_name,
    Employees.salary,
    Departments.name AS department_name
FROM Employees
LEFT JOIN Departments ON Employees.department_id = Departments.department_id;


# 17. הצג רק עובדים שאין להם מחלקה:
SELECT
    Employees.emp_id,
    Employees.name AS employee_name
FROM Employees
WHERE department_id IS NULL;


# 18. ספור כמה עובדים יש:
SELECT
    COUNT(*) AS total_employees
FROM Employees;


# 19. מצא את המשכורת הממוצעת של כל עובד:
SELECT
    AVG(salary) AS average_salary
FROM Employees;


# 20. מצא את המשכורת הגבוהה ביותר בכל מחלקה (עם שם העובד):
SELECT
    Departments.name AS department_name,
    Employees.name AS employee_name,
    MAX(Employees.salary) AS highest_salary
FROM Employees
INNER JOIN Departments ON Employees.department_id = Departments.department_id
GROUP BY Departments.department_id;


# 21. הצג את העובדים לפי רמת seniority, בסדר עולה, עם פרטי המחלקה:
SELECT
    Employees.name AS employee_name,
    Employees.seniority,
    Departments.name AS department_name
FROM Employees
LEFT JOIN Departments ON Employees.department_id = Departments.department_id
ORDER BY Employees.seniority ASC;


# 22. מצא את המשכורת הממוצעת לכל רמת seniority:
SELECT
    seniority,
    AVG(salary) AS average_salary
FROM Employees
GROUP BY seniority;




















