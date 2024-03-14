--Пошук можна здійснити запустивши файл starter_query.py, вказавши номер запиту (1-10), fullname студента.

-- Знаходимо список курсів, які певному студенту читає певний викладач.
SELECT DISTINCT subjects.name AS course_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON subjects.id = subjects.teacher_id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.fullname = :students_fullname AND teachers.fullname = :teachers_fullname;
