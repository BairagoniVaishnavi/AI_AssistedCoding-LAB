CREATE DATABASE IF NOT EXISTS college;
USE college;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

INSERT INTO students (name, age, course)
VALUES 
('Vaishnavi', 21, 'CSE'),
('Rahul', 22, 'ECE'),
('Anjali', 20, 'IT');

SELECT * FROM students;