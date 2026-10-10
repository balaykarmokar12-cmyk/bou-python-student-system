-- File: database.sql
CREATE DATABASE bou_sms_balay;
USE bou_sms_balay;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stu_id VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    program VARCHAR(20) DEFAULT 'DCSA',
    semester VARCHAR(20) DEFAULT '3rd Semester',
    center VARCHAR(100) DEFAULT 'Daffodil Institute of IT (DIIT), Chittagong'
);

INSERT INTO students (stu_id, name) VALUES ('24150892008', 'Balay Karmaker');
