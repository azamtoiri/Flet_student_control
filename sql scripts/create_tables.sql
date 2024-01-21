-- Таблица курсов
CREATE TABLE Courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(100) NOT NULL,
  course_description TEXT
);

-- Таблица пользователей
CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  last_name VARCHAR(50) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  middle_name VARCHAR(50),
  age INT,
  group_name VARCHAR(50),
  course INT,
  email VARCHAR(100) NOT NULL UNIQUE,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(50) NOT NULL,
  is_staff BOOLEAN,
  is_superuser BOOLEAN,
  created_at DATE NOT NULL
);

-- Таблица записей на курсы (связывает студентов и курсы)
CREATE TABLE Enrollments (
  enrollment_id INT PRIMARY KEY,
  user_id INT,
  course_id INT,
  enrollment_date DATE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Таблица оценок
CREATE TABLE Grades (
  grade_id INT PRIMARY KEY,
  enrollment_id INT,
  grade_value FLOAT,
  grade_date DATE NOT NULL,
  FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id)
);
