""" List Comprehensions. Давайте дізнаємося про розуміння списків! Вам дано три цілі числа, x,
y i z які представляють
розміри кубоїда разом із цілим числом n. Надрукуйте список усіх можливих координат, заданих (i,j,k)
на тривимірній сітці, де сума i+j+k не дорівнює n. Тут, 0<=i<=x;0<=j<=y;0<=k<=z. Будь ласка,
використовуйте розуміння списків, а не кілька циклів, як навчальну вправу. """

# def func(x, y, z, n):
#     result = []
#     for i in range(x + 1):
#         for j in range(y + 1):
#             for k in range(z + 1):
#                 if i + j + k != n:
#                     result.append([i, j, k])
#     print(result)
#
#
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     func(x, y, z, n)

""" Find the Runner-Up Score! Враховуючи таблицю результатів учасників для вашого 
Університетського дня спорту, ви повинні знайти результат, який посідає друге місце. Вам дають n 
балів. Збережіть їх у списку та знайдіть оцінку гравця, який посів друге місце.
Формат введення
Перший рядок містить n. Другий рядок містить масив A[] з n цілих чисел, кожне з яких розділено 
пробілом."""

# def find_second_largest(n, arr):
#     if n == len(arr):
#         unique_elements = list(set(arr))
#         for i in arr:
#             if i not in unique_elements:
#                 unique_elements.append(i)
#         sorted_elements = sorted(unique_elements)
#         print(sorted_elements[-2])
#     else:
#         print("n != len(arr)")
#
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     find_second_largest(n, arr)

""" Nested Lists. Давши імена та оцінки для кожного учня в класі N учнів, збережіть їх у 
вкладеному списку та надрукуйте імена будь-якого учня (учнів), які мають другий найнижчий бал.
Примітка. Якщо є кілька студентів із другою найнижчою оцінкою, упорядкуйте їхні імена в 
алфавітному порядку та друкуйте кожне ім’я з нового рядка.
Приклад:
records = [['chi',20.0],['beta',50.0],['alpha',50.0]]
Упорядкований список балів є [20.0,50.0], тому другий найнижчий бал 50.0. Є два 
студенти з балом: 'beta', 'alpha'. Імена в алфавітному порядку друкуються так: 'alpha', 'beta'. """

# def get_second_lowest_students(students):
#     # Збираємо всі бали в окремий список
#     scores = sorted({score for name, score in students})
#     # Знаходимо другий найнижчий бал
#     second_lowest_score = scores[1]
#     # Збираємо імена студентів з другим найнижчим балом
#     second_lowest_students = [name for name, score in students if score == second_lowest_score]
#     # Сортуємо імена в алфавітному порядку
#     second_lowest_students.sort()
#     # Виводимо імена студентів
#     for student in second_lowest_students:
#         print(student)
#
# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     get_second_lowest_students(students)

""" Finding the percentage. Наданий фрагмент коду читатиметься в словнику, що містить пари  
ключ/значення ім’я:[знаки] для списку студентів. Надрукуйте середнє значення масиву оцінок для  
наданого імені студента, показуючи 2 знаки після коми. 
Приклад: 
 mark skey: value pairs are
 'alpha': [20, 30, 40]
 'beta': [30, 50, 70]
 query_name = 'beta'
 query_name є "бета ". середній бал бета-версії становить (30+50+70)/3 = 50.0 
Формат введення:
Перший рядок містить ціле число n, кількість записів студентів. Наступний n рядки містять імена та 
оцінки, отримані учнем, кожне значення розділене пробілом. Останній рядок містить query_name,  
ім’я студента для запиту."""


# def average_value(student_marks, query_name):
#     scores = student_marks[query_name]
#     avg = sum(scores) / len(scores)
#     print("{:.2f}".format(avg))
#
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     average_value(student_marks, query_name)

""" Lists. Розглянемо список (list=[]). Ви можете виконувати такі команди:
insert i e: Вставити ціле числона e на позиції i.
print: роздрукувати список.
remove e: Видалити перше входження цілого числа e.
append e: Вставити ціле число e в кінці списку.
sort: сортувати список.
pop: витягнути останній елемент зі списку.
reverse: перевернути список.
Ініціалізуйте свій список і прочитайте значення n а потім n рядки команд, де кожна команда буде 
з 7 перелічених вище типи. Перегляньте кожну команду по порядку та виконайте відповідну 
операцію у своєму списку.
Приклад:
N = 4
append 1
append 2
insert 3 1
print
- append 1: Додаток 1 до списку, arr=[1].
- append 2: Додаток 2 до списку, arr=[1, 2].
- insert 3 1: Вставказа 3 за індексом 1, arr=[1, 3, 2].
- print: надрукувати масив.
Вихід:
[1, 3, 2]"""

def list_operation(n):
    arr=[]
    operation = {}
    for _ in range(n):
        op, *line = input().split()

        integer = list(map(float, line))
        operation[op] = integer

def operation():
    if _ == insert:
        



    # insert
    # remove
    # append
    # sort
    # pop
    # reverse
    # print

if __name__ == '__main__':
    n = int(input())
    list_operation(n)