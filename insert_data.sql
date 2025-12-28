USE project1;


//sample insertion


INSERT INTO Students (name, department) VALUES
('Aarav Sharma', 'Computer Science'),
('Diya Patel', 'Information Technology'),
('Rohan Mehta', 'Mechanical'),
('Neha Singh', 'Computer Science');

INSERT INTO Subjects (subject_name) VALUES
('Data Structures'),
('Database Systems'),
('Operating Systems');

INSERT INTO Marks (student_id, subject_id, score, semester) VALUES
(1, 1, 85, 1),
(1, 2, 78, 1),
(2, 1, 72, 1),
(3, 3, 88, 1),
(4, 2, 91, 1);
