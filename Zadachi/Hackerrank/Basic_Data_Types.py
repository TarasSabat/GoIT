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

def get_second_lowest_students(students):
    # Збираємо всі бали в окремий список
    scores = sorted({score for name, score in students})
    # Знаходимо другий найнижчий бал
    second_lowest_score = scores[1]
    # Збираємо імена студентів з другим найнижчим балом
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    # Сортуємо імена в алфавітному порядку
    second_lowest_students.sort()
    # Виводимо імена студентів
    for student in second_lowest_students:
        print(student)

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    get_second_lowest_students(students)
