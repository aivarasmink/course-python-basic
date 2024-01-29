INSERT INTO student (id, name, last_name, birthday, city)
VALUES (1, 'John', 'Doe', '1980-01-01', 'New York');
INSERT INTO student (id, name, last_name, birthday, city)
VALUES (2, 'Jane', 'Voe', '1999-01-01', 'Vilnius');

SELECT * FROM student;
SELECT * FROM student WHERE city = 'New York';