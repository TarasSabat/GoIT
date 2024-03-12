-- Пошук можна здійснити запустивши файл starter_query.py та вказавши номер запиту (1-10).

-- Знаходимо студента із найвищим середнім балом з певного предмета.
SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
where g.subject_id = 1   -- Вказуємо предмет, для якого шукається середній бал студента
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;