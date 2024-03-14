-- Пошук можна здійснити запустивши файл starter_query.py, вказавши номер запиту (1-10), id предмету (1-5) та id групи (1-3).

-- Знаходимо оцінки студентів у окремій групі з певного предмета.
SELECT students.fullname, grades.grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE group_id = :group_id AND subject_id = :subject_id;





