-- Вставка тестовых данных в таблицу Users
INSERT INTO Users (user_id, last_name, first_name, middle_name, age, "group", course, email, username, password, is_staff, is_superuser)
VALUES
  (1, 'Doe', 'John', 'Middle', 22, 'GroupA', 2, 'john.doe@example.com', 'john123', 'password123', false, false),
  (2, 'Smith', 'Jane', 'Anne', 23, 'GroupB', 3, 'jane.smith@example.com', 'jane123', 'password456', false, false),
  (3, 'Johnson', 'Bob', 'Robert', 24, 'GroupC', 1, 'bob.johnson@example.com', 'bob123', 'password789', true, false);

-- Вставка тестовых данных в таблицу Courses (оставляем прежние данные)
INSERT INTO Subjects (subject_id, subject_name, description)
VALUES
  (1, 'Introduction to Programming', 'Learn the basics of programming'),
  (2, 'Database Management', 'Explore the world of database systems'),
  (3, 'Web Development', 'Build dynamic and interactive websites');

-- Вставка тестовых данных в таблицу Enrollments
INSERT INTO Enrollments (enrollment_id, user_id, subject_id, enrollment_date)
VALUES
  (1, 1, 1, '2023-01-15'),
  (2, 1, 2, '2023-01-16'),
  (3, 2, 3, '2023-01-17'),
  (4, 3, 1, '2023-01-18');

-- Вставка тестовых данных в таблицу Grades
INSERT INTO Grades (grade_id, enrollment_id, grade, "date")
VALUES
  (1, 1, 90, '2023-02-01'),
  (2, 2, 85, '2023-02-02'),
  (3, 3, 95, '2023-02-03'),
  (4, 4, 88, '2023-02-04');
