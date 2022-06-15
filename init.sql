USE cc;

DROP TABLE IF EXISTS fee;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS students;

CREATE TABLE fee (
  id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  total_fee int NOT NULL,
  sub_fee int NOT NULL,
  rem_fee int NOT NULL,
  roll_no varchar(20) NOT NULL
);

ALTER TABLE fee AUTO_INCREMENT=5;

INSERT INTO fee values (1, 131000, 131000, 0, '18PD36'),
(2, 131000, 500, 130500, '18CA02'),
(3, 131000, 0, 131000, '19PW01'),
(4, 131000, 0, 131000, '19PT15');

CREATE TABLE sessions (
  id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title varchar(20) NOT NULL
);

ALTER TABLE sessions AUTO_INCREMENT=15;

INSERT INTO sessions VALUES (1, 'MSC-2018'),
(2, 'MSC-2017'),(3, 'MSC-2016'),(4, 'MSC-2019'),(5, 'MSC-2021'),
(6, 'MSC-2020'),(7, 'IT-2018'),(8, 'IT-2017'),(9, 'IT-2016'),
(10, 'MCA-2018'),(11, 'MCA-2019'),(12, 'MCA-2020'),
(13, 'PhD-2022');

CREATE TABLE students(
  s_id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
  fname varchar(50) NOT NULL,
  lname varchar(50),
  contact varchar(15) NOT NULL,
  roll_no varchar(20) NOT NULL,
  session varchar(20) NOT NULL
);

ALTER TABLE students AUTO_INCREMENT=6;

insert into students values (1,'Snehaa','S','9786590450','18PD36','MSC-2018'),(2,'Janet','G','4657809120','18PD13','MSC-2018'),
(3,'Akshay','Kumar','4657559120','19PT15','MSC-2019'),(4,'johny','B','1157809120','19PW01','MSC-2019'),
(5,'Keshav','Ajay','4634569120','18CA02','MCA-2018');