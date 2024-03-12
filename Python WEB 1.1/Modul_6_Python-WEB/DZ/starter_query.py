import sqlite3

request_number = int(input("Enter the request number >>> "))
if request_number == 1:
    a = "query_1.sql"
elif request_number == 2:
    a = "query_2.sql"
elif request_number == 3:
    a = "query_3.sql"
    # Введення значення subject_id
    subject_id = input("Введіть id предмета >>> ")
elif request_number == 4:
    a = "query_4.sql"
elif request_number == 5:
    a = "query_5.sql"
    # Введення значення teacher_id
    teacher_id = input("Введіть id викладача >>> ")
elif request_number == 6:
    a = "query_6.sql"
    # Введення значення group_id
    group_id = input("Введіть id групи >>> ")
elif request_number == 7:
    a = "query_7.sql"
elif request_number == 8:
    a = "query_8.sql"
elif request_number == 9:
    a = "query_9.sql"
elif request_number == 10:
    a = "query_10.sql"
else:
    print("Invalid request number")
# Підключення до бази даних SQLite
conn = sqlite3.connect("DZ_Mod_6")

# Створення курсора
cursor = conn.cursor()

# Зчитування вмісту файлу query_number.sql
with open(a, "r") as file:
    sql = file.read()


# Виконання SQL-запиту для subject_id (query_3.sql)
def execute_query_with_subject_id(subject_id=None):
    if subject_id is not None:
        cursor.execute(sql, (subject_id,))
    else:
        cursor.execute(sql)


# Виклик функції з аргументом subject_id, якщо він був визначений
if "subject_id" in locals() and request_number == 3:
    execute_query_with_subject_id(subject_id)


# Виконання SQL-запиту для teacher_id (query_5.sql)
def execute_query_with_teacher_id(teacher_id=None):
    if teacher_id is not None:
        cursor.execute(sql, (teacher_id,))
    else:
        cursor.execute(sql)


# Виклик функції з аргументом teacher_id, якщо він був визначений
if "teacher_id" in locals() and request_number == 5:
    execute_query_with_teacher_id(teacher_id)


# Виконання SQL-запиту для group_id (query_6.sql)
def execute_query_with_teacher_id(group_id=None):
    if group_id is not None:
        cursor.execute(sql, (group_id,))
    else:
        cursor.execute(sql)


# Виклик функції з аргументом group_id, якщо він був визначений
if "group_id" in locals() and request_number == 6:
    execute_query_with_teacher_id(group_id)

# Отримання результатів (якщо потрібно)
results = cursor.fetchall()
for row in results:
    print(row)

# Збереження змін у базі даних
conn.commit()

# Закриття курсора та з'єднання з базою даних
cursor.close()
conn.close()
