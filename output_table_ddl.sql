
DROP TABLE IF EXISTS ADMIN.STUDENTS CASCADE;
CREATE TABLE ADMIN.STUDENTS 
(
STUDENT_NAME  varchar(22),
STUDENT_ID  DOUBLE PRECISION,
SPANISH  varchar(1),
MONDAY  varchar(1),
TUESDAY  varchar(1) NOT NULL,
WEDNESDAY  varchar(1) NOT NULL,
THURSDAY  varchar(1),
FRIDAY  varchar(1) NOT NULL
);

DROP TABLE IF EXISTS GRADES.RESULTS CASCADE;
CREATE TABLE GRADES.RESULTS 
(
STUDENT_ID  DOUBLE PRECISION,
CLASS_ID  Integer,
TEACHER_ID  DOUBLE PRECISION NOT NULL,
MARKS  DOUBLE PRECISION,
RESULT  BOOLEAN
);
