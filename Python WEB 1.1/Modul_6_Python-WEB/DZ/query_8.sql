-- Пошук можна здійснити запустивши файл starter_query.py, вказавши номер запиту (1-10) та id викладача (1-5).

-- Знаходимо середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.fullname AS teacher_name, AVG(grades.grade) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teacher_id = :teacher_id; 

