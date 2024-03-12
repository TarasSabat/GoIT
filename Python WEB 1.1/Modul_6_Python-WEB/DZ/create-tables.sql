-- Таблиця груп
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

-- Таблиця студентів
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(150) NOT NULL,
  group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE
);

-- Таблиця викладачів
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(150) NOT NULL
);

-- Таблиця предметів
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(175) NOT NULL,
  teacher_id INTEGER REFERENCES teachers(id) ON DELETE CASCADE
);

-- Таблиця оцінок
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
  subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
  grade INTEGER CHECK (grade >= 0 AND grade <= 100),
  grade_date DATE NOT NULL
);
