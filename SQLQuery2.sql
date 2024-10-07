CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Country VARCHAR(50),
    Program VARCHAR(100),
    YearOfStudy INT
);

-- Inserting data into the Students table
INSERT INTO Students (StudentID, FirstName, LastName, Age, Gender, Country, Program, YearOfStudy) 
VALUES
(1, 'Amina', 'Ahmed', 21, 'Female', 'Nigeria', 'Computer Science', 3),
(2, 'Kofi', 'Mensah', 19, 'Male', 'Ghana', 'Mechanical Engineering', 2),
(3, 'Fatima', 'Hassan', 22, 'Female', 'Kenya', 'Business Administration', 4),
(4, 'Samuel', 'Ndlovu', 20, 'Male', 'South Africa', 'Civil Engineering', 2),
(5, 'Aisha', 'Bakari', 18, 'Female', 'Tanzania', 'Economics', 1),
(6, 'Abdoul', 'Diouf', 23, 'Male', 'Senegal', 'Information Technology', 4),
(7, 'Maryam', 'Elamin', 21, 'Female', 'Sudan', 'Biomedical Science', 3),
(8, 'Kwame', 'Owusu', 19, 'Male', 'Ghana', 'Electrical Engineering', 1),
(9, 'Zainab', 'Yusuf', 20, 'Female', 'Nigeria', 'Law', 2),
(10, 'Omar', 'Ali', 22, 'Male', 'Somalia', 'Computer Science', 4);
