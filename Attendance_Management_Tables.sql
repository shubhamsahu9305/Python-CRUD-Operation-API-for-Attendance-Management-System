CREATE DATABASE student_attendance_management;

USE student_attendance_management;

CREATE TABLE users(
id INT PRIMARY KEY AUTO_INCREMENT,
user_type VARCHAR(20) NOT NULL,
full_name VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
user_password VARCHAR(255) NOT NULL,
submitted_by INT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX idx_username
ON users (username, email);

CREATE TABLE courses(
id INT PRIMARY KEY AUTO_INCREMENT,
course_name VARCHAR(255) NOT NULL,
department_id INT NOT NULL UNIQUE,
semester INT NOT NULL,
class VARCHAR(255) NOT NULL,
lecture_hours DECIMAL(4,2) NOT NULL,
submitted_by INT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX idx_classname
ON courses (class);

CREATE TABLE attendance_log(
id INT PRIMARY KEY AUTO_INCREMENT,
student_id INT NOT NULL UNIQUE,
course_id INT NOT NULL,
present BOOL NOT NULL,
submitted_by INT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
FOREIGN KEY (course_id) REFERENCES courses(id),
FOREIGN KEY (submitted_by) REFERENCES users(id)
);

CREATE TABLE departments(
id INT PRIMARY KEY,
department_name VARCHAR(255) NOT NULL,
submitted_by INT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
FOREIGN KEY (id) REFERENCES courses(department_id)
);

CREATE INDEX idx_departmentname
ON departments (department_name);

CREATE TABLE students(
id INT PRIMARY KEY,
full_name VARCHAR(255) NOT NULL,
department_id INT NOT NULL,
class VARCHAR(255) NOT NULL,
submitted_by INT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
FOREIGN KEY (id) REFERENCES attendance_log(student_id)
);

CREATE INDEX idx_studentname
ON students (full_name, class);
