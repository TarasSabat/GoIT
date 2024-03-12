-- Пошук можна здійснити запустивши файл starter_query.py та вказавши номер запиту (1-10) та id викладача (1-5).

-- Знаходимо які курси читає певний викладач.
SELECT subjects.name AS course_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = :teacher_id; -- Вказуємо id викладача, для якого здійснюємо пошук