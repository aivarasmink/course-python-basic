CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
surname VARCHAR(50)
);

CREATE TABLE cursies (
id INTEGER PRIMARY KEY,
pavadinimas VARCHAR(50),
discription TEXT
);

CREATE TABLE STUDENTS_CURSIES (
id INTEGER PRIMARY KEY,
students_id INTEGER REFERENCES students(id),
cursies_id INTEGER REFERENCES cursies(id)
);


