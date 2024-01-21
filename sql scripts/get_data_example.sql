-- SQL-запрос для получения информации о студенте, его курсах и оценках
SELECT
  Users.user_id,
  Users.first_name,
  Users.last_name,
  Subjects.subject_name,
  Grades.grade,
  Grades.date
FROM
  Users
JOIN
  Enrollments ON Users.user_id = Enrollments.user_id
JOIN
  Subjects ON Enrollments.subject_id = Subjects.subject_id
JOIN
  Grades ON Enrollments.enrollment_id = Grades.enrollment_id
WHERE
  Users.user_id = 1; -- Замените на нужный user_id
