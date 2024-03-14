import sqlite3


request_number = int(input("Enter the request number >>> "))
if request_number == 1:
    a = "query_1.sql"
elif request_number == 2:
    a = "query_2.sql"
elif request_number == 3:
    a = "query_3.sql"
    # Введення значення subject_id
    id = input("Введіть id предмета >>> ")
elif request_number == 4:
    a = "query_4.sql"
elif request_number == 5:
    a = "query_5.sql"
    # Введення значення teacher_id
    id = input("Введіть id викладача >>> ")
elif request_number == 6:
    a = "query_6.sql"
    # Введення значення group_id
    id = input("Введіть id групи >>> ")
elif request_number == 7:
    a = "query_7.sql"
    # Введення значення group_id
    id_1 = input("Введіть id групи >>> ")
    # Введення значення subject_id
    id_2 = input("Введіть id предмета >>> ")
elif request_number == 8:
    a = "query_8.sql"
    # Введення значення teacher_id
    id = input("Введіть id викладача >>> ")
elif request_number == 9:
    a = "query_9.sql"
    # Введення значення fullname
    id = input("Введіть fullname студента >>> ")
elif request_number == 10:
    a = "query_10.sql"
    # Введення значення students_fullname
    id_1 = input("Введіть fullname студента >>> ")
    # Введення значення teachers_fullname
    id_2 = input("Введіть fullname викладача >>> ")
else:
    print("Недійсний номер запиту")

# Підключення до бази даних SQLite
conn = sqlite3.connect("DZ_Mod_6")

# Створення курсора
cursor = conn.cursor()

# Зчитування вмісту файлу query_number.sql
with open(a, "r") as file:
    sql = file.read()


# Виконання SQL-запиту для query_3.sql, query_5.sql, query_6.sql, query_8.sql, query_9.sql


def execute_query_3_5_6_8_9(id=None):
    if id is not None:
        cursor.execute(sql, (id,))
    else:
        cursor.execute(sql)


# Виклик функції з аргументом, якщо він був визначений
if "id" in locals() and request_number in (3, 5, 6, 8, 9):
    execute_query_3_5_6_8_9(id)
elif request_number in (1, 2, 4):
    execute_query_3_5_6_8_9()


# Виконання SQL-запиту для query_7.sql, query_10.sql
def execute_query_7_10(id_1=None, id_2=None):
    if id_1 and id_2 is not None:
        cursor.execute(sql, (id_1, id_2))
    else:
        cursor.execute(sql)


# Виклик функції з аргументом, якщо він був визначений
if "id_1" and "id_2" in locals() and request_number in (7, 10):
    execute_query_7_10(id_1, id_2)

# Отримання результатів (якщо потрібно)
results = cursor.fetchall()
for row in results:
    print(row)

# Збереження змін у базі даних
conn.commit()

# Закриття курсора та з'єднання з базою даних
cursor.close()
conn.close()
