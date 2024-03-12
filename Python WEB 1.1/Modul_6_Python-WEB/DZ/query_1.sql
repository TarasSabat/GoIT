-- Пошук можна здійснити запустивши файл starter_query.py та вказавши номер запиту (1-10).

-- Знаходимо 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;