-- Пошук можна здійснити запустивши файл starter_query.py та вказавши номер запиту (1-10) та id предмета (1-5).

-- Знаходимо середній бал у групах з певного предмета.
SELECT 
    groups.name AS group_name,
    AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = :subject_id    -- Вказуємо id предмета, для якого шукається середній бал груп
GROUP BY groups.name;
