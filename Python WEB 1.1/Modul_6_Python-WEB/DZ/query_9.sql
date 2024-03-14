-- Пошук можна здійснити запустивши файл starter_query.py, вказавши номер запиту (1-10) та fullname студента (1-30).

-- Знаходимо список курсів, які відвідує студент.
SELECT DISTINCT subjects.name AS course_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE fullname = :fullname;






